# 💬 RAG Chatbot with Context Memory

A conversational AI chatbot using Retrieval-Augmented Generation (RAG) with memory. Built with LangChain, OpenAI, FAISS, and Streamlit.

---

## 🧠 Features

- Context-aware Q&A from custom documents
- Uses FAISS vector index for fast semantic search
- Dual interface: Streamlit (frontend) + FastAPI (backend)
- LangChain memory for conversational flow

---

## 📁 Project Structure

rag-chatbot/
├── data/docs/ # Your document PDFs or text files
├── src/
│ ├── chatbot_app.py # Streamlit UI
│ └── api.py # FastAPI backend
├── vector_store/ # FAISS index stored here

---

## 🚀 How to Run

### Install dependencies
bash
pip install -r requirements.txt

Start the chatbot (Streamlit UI)

streamlit run src/chatbot_app.py
Optional: Start backend API
uvicorn src.api:app --reload

📚 Data
Store your PDFs or .txt files in data/docs/
FAISS index will be created in vector_store/

🛠️ Tech Stack
Python, LangChain, OpenAI

FAISS (vector DB), Streamlit

FastAPI (backend), PyPDF / Text loaders