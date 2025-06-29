from fastapi import APIRouter
from mcp_scraper.scraper import scrape_cves
from db.chroma_client import save_embeddings
from db.mysql_client import save_metadata

mcp_router = APIRouter()

@mcp_router.post("/scrape-cves")
async def scrape_and_store():
    cves = scrape_cves()

    for cve in cves:
        # Save to VectorDB
        save_embeddings(cve['cve_id'], cve['description'])

        # Save to Relational DB
        save_metadata(cve)

    return {"status": "success", "cves_scraped": len(cves)}

