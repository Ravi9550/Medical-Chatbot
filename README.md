# 🏥 Medical Chatbot using FAISS & LangChain  

## 📌 Overview  
This is an AI-powered **Medical Chatbot** that efficiently retrieves and answers medical queries using **FAISS, LangChain, and Llama-2**.  

## 🚀 Features  
 **Fast Retrieval** – Uses FAISS for efficient medical document search.  
 **Accurate Responses** – Powered by **Llama-2 (7B-Chat)** for context-aware answers.  
 **Medical Data Processing** – Extracts knowledge from medical research papers.  
 **Scalable Architecture** – Optimized for real-world healthcare applications.  

## 🏗️ Tech Stack  
- **LangChain** – Framework for LLM-based retrieval.  
- **FAISS** – Vector search for document retrieval.  
- **Hugging Face MiniLM** – Generates text embeddings.  
- **Llama-2** – Large Language Model for response generation.  
- **PyPDFLoader** – Extracts data from medical documents.  

## 📜 Installation  
1️⃣ Clone the repository:  
   ```bash
   git clone https://github.com/Ravi9550/Medical-Chatbot.git
   cd Medical-Chatbot
   ```
2️⃣ Create a Virtual Environment (Optional but Recommended): 
   ```bash
   python -m venv env
  ```
3️⃣ Install Dependencies
  ```bash
    pip install -r requirements.txt
  ```
4️⃣ Run the Streamlit App
   ```bash
   streamlit run app.py
   ```

🖥️ How It Works
1️⃣ User enters a medical query in the chatbot UI.

2️⃣ FAISS retrieves the most relevant medical documents.

3️⃣ Llama-2 generates a response using retrieved data.

4️⃣ The chatbot displays the response in the Streamlit UI.


💡 Future Enhancements
🌍 Multilingual Support - Support non-English medical queries.

🎤 Voice-Based Queries - Enable voice-based medical queries.

📡 Integration with WHO & CDC APIs - Connect with WHO & CDC databases

🤝 Contributing
Feel free to submit issues or pull requests!
