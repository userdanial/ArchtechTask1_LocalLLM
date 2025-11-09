import streamlit as st
import requests
import json

# App title and layout
st.set_page_config(page_title="Local LLM Chat", page_icon="💬", layout="centered")
st.title("💬 Chat with Local LLM (Ollama)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for conversation history
with st.sidebar.expander("🕙 Conversation History", expanded=True):
    if st.session_state.messages:
        for msg in st.session_state.messages:
            role = "🧑 You" if msg["role"] == "user" else "🤖 Bot"
            st.markdown(f"**{role}:** {msg['content']}")
    else:
        st.markdown("_No messages yet._")

# Sidebar button to reset conversation
if st.sidebar.button("🧹 Reset Conversation"):
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**🧑 You:** {msg['content']}")
    else:
        st.markdown(f"**🤖 Bot:** {msg['content']}")

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Prepare payload for Ollama
    payload = {"model": "gemma3", "prompt": user_input}

    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload, stream=True)
        reply = ""

        # Read streaming response
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                if "response" in data:
                    reply += data["response"]

    except Exception as e:
        reply = f"Error: {e}"

    # Add bot reply to history
    st.session_state.messages.append({"role": "assistant", "content": reply})

    # Rerun the app to display new messages
    st.rerun()
