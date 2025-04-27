from fastapi import APIRouter
from pydantic import BaseModel
from db.chroma_client import query_embeddings
from llm.ollama_client import generate_response

chat_router = APIRouter()

class ChatRequest(BaseModel):
    question: str

@chat_router.post("/chat")
async def chat_rag(request: ChatRequest):
    # 1. Retrieve matching CVEs from ChromaDB
    context = query_embeddings(request.question)

    # 2. Prepare context string
    combined_context = "\n\n".join([
        f"{doc}" for doc in context['documents'][0]
    ])

    # 3. Generate final answer with Ollama
    final_prompt = f"Using the following CVE information:\n\n{combined_context}\n\nAnswer the question: {request.question}"
    answer = generate_response(final_prompt)

    return {"answer": answer}

