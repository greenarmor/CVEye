from fastapi import FastAP0
from mcp_scraper.mcp_server import mcp_router
from llm.rag_chain import chat_router

app = FastAPI(
    title="CVEye AI Chat",
    description="AI Chatbot with CVE Knowledge",
    version="0.1.0",
)

# MCP scrape routes
app.include_router(mcp_router, prefix="/api")

# Chat langgraph routes
app.include_router(chat_router, prefix="/api")

