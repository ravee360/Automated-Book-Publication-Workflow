import chromadb

# ✅ Create a persistent ChromaDB client
client = chromadb.PersistentClient(path="./chroma_store")
collection = client.get_or_create_collection(name="chapters")

def store_text_version(
    chapter_id: str,
    text: str,
    source: str,
    stage: str,
    version: int,
    reward: int | None = None,
    feedback: str | None = None
):
    full_id = f"{chapter_id}_{stage}_v{version}"
    metadata = {
        "source": source,
        "stage": stage,
        "version": version,
        "reward": reward,
    }
    if feedback:
        metadata["human_feedback"] = feedback

    collection.upsert(
        documents=[text],
        metadatas=[metadata],
        ids=[full_id]
    )
    print(f"✅ Stored: {full_id}")

