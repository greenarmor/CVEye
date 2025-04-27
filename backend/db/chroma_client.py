import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("cves")

def save_embeddings(cve_id, description):
    collection.add(
        documents=[description],
        metadatas=[{"cve_id": cve_id}],
        ids=[cve_id]
    )

def query_embeddings(query_text, top_k=3):
    results = collection.query(
        query_texts=[query_text],
        n_results=top_k
    )
    return results

