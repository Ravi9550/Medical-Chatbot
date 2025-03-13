from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import CTransformers

# Step 1: Load PDF documents
def load_pdf(data_path):
    loader = DirectoryLoader(data_path, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents

extracted_data = load_pdf("data/")

# Step 2: Split text into chunks
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks

text_chunks = text_split(extracted_data)
print(f"Number of text chunks: {len(text_chunks)}")

# Step 3: Load embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
print("Embeddings Loaded Successfully!")

# Step 4: Save FAISS Index (Only Run Once)
try:
    vector_store = FAISS.load_local("faiss_index", embeddings)
    print(" FAISS index loaded successfully!")
except:
    print("⚡ FAISS index not found. Creating new FAISS index...")
    vector_store = FAISS.from_documents(text_chunks, embeddings)
    vector_store.save_local("faiss_index")  
    print("FAISS index created and saved!")

# Step 5: Define Prompt Template
prompt_template = """
Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain_type_kwargs = {"prompt": PROMPT}

# Step 6: Load LLM Model
llm = CTransformers(
    model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
    model_type="llama",
    config={'max_new_tokens': 512, 'temperature': 0.8}
)


qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_store.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs
)

print("Medical chatbot is ready!")
