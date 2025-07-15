from db.store_chapters import collection
from agents.reward_model import feedback_to_reward_llm

def update_reward_and_feedback(chapter_full_id: str, feedback_text: str):
    """
    Update the ChromaDB document's metadata for a given versioned chapter ID (e.g., 'chapter1_spun_v1').
    """
    reward_score = feedback_to_reward_llm(feedback_text)

    collection.update(
        ids=[chapter_full_id],
        metadatas=[{
            "reward": reward_score,
            "human_feedback": feedback_text
        }]
    )

    print(f"✅ Updated reward ({reward_score}) and feedback for '{chapter_full_id}'")
