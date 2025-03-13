import streamlit as st
from trial import qa  


st.set_page_config(page_title="Medical Chatbot", page_icon="💬", layout="wide")


if "chat_sessions" not in st.session_state:
    st.session_state.chat_sessions = {}
if "selected_session" not in st.session_state:
    st.session_state.selected_session = None


st.sidebar.title("💬 Chat Sessions")

# New Chat Button
if st.sidebar.button("➕ New Chat"):
    session_id = f"Chat {len(st.session_state.chat_sessions) + 1}"
    st.session_state.chat_sessions[session_id] = []
    st.session_state.selected_session = session_id


for session in st.session_state.chat_sessions:
    if st.sidebar.button(session):
        st.session_state.selected_session = session


@st.cache_data
def get_answer(query):
    return qa(query)["result"]

# Main Chat UI
st.title("🩺 Medical Chatbot")

if st.session_state.selected_session is None:
    st.write(" Select a chat session or start a new chat.")
else:
    st.subheader(st.session_state.selected_session)

    
    chat_history = st.session_state.chat_sessions[st.session_state.selected_session]
    for role, msg in chat_history:
        st.markdown(f"**{role}:** {msg}")

   
    user_query = st.text_input("Type your question here...", key=st.session_state.selected_session)

    if user_query:
        with st.spinner("Thinking..."):
            response = get_answer(user_query)

            chat_history.append(("You", user_query))
            chat_history.append(("Bot", response))

            st.markdown(f"**🤖 Bot:** {response}")
