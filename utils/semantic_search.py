from db.store_chapters import collection

def search_similar_chapters(query: str, top_k=3):
    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )

    print("\n🔍 Semantic Search Results:")
    for doc, metadata in zip(results["documents"][0], results["metadatas"][0]):
        print(f"\n📘 Stage: {metadata.get('stage')} | Version: {metadata.get('version')}")
        print(f"📜 Text Preview:\n{doc[:500]}...\n{'-'*40}")


def show_all_versions(chapter_id: str):
    results = collection.get()

    print(f"\n📚 All stored versions for: {chapter_id}")

    for doc, meta, doc_id in zip(results['documents'], results['metadatas'], results['ids']):
        if doc_id.startswith(chapter_id):
            print(f"\n🆔 ID: {doc_id}")
            print(f"🗂️  Stage: {meta.get('stage')}, Version: {meta.get('version')}")
            print(f"⭐ Reward: {meta.get('reward')} | ✍️ Feedback: {meta.get('human_feedback')}")
            print(f"📜 Text Preview:\n{doc[:300]}...\n{'-'*50}")
