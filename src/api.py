from fastapi import FastAPI
from pydantic import BaseModel
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "RAG Chatbot API is running"}

@app.post("/ask")
def ask_question(request: QueryRequest):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.load_local("vector_store", embeddings)
    llm = ChatOpenAI(temperature=0.2)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())
    answer = qa_chain.run(request.query)
    return {"answer": answer}

# For Streamlit
def get_answer(query):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.load_local("vector_store", embeddings)
    llm = ChatOpenAI(temperature=0.2)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())
    return qa_chain.run(query)
