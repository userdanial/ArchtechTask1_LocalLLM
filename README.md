# ArchtechTask1_LocalLLM
# 💬 Local LLM Chat App (Streamlit + Ollama)

A simple and interactive **Streamlit web interface** to chat with a **locally installed large language model (LLM)** using Ollama. The app allows you to input queries, get responses from the model, view conversation history, and reset the chat.

---

## **Features**

- Chat with a **local LLM** (Ollama) without the internet.  
- **Conversation history panel** in the sidebar.  
- **Reset button** to clear chat history.  
- Clean and interactive **Streamlit interface**.  
- Works fully **offline** once the model is installed.  

---

## **Installation**

1. Clone this repository:

```bash
git clone https://github.com/your-username/local-llm-chat.git
cd local-llm-chat

##Method
###Create and activate a virtual environment (recommended):

python -m venv venv
venv/Scripts/activate.ps1

##Install dependencies:
pip install streamlit requests

# Install and run your Ollama local LLM (e.g., gemma3) as per Ollama instructions

##Usage
### Run the Streamlit app:
streamlit run app.py

##Notes
Use the text input box to ask questions.
View conversation history in the sidebar.
Click “Reset Conversation” to clear the chat.


The app works entirely offline once the model is installed locally.
Response speed depends on your hardware (CPU/GPU) and the size of the model.
No internet/Wi-Fi is needed for chat; only required for initial model download.
