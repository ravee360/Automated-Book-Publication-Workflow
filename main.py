from agents.llm_writer import spin_text
from db.store_chapters import store_text_version
from db.update_metadata import update_reward_and_feedback
from utils.voice_interface import get_voice_input, speak_text, choose_input_mode, choose_output_mode
from utils.semantic_search import search_similar_chapters

chapter_id = "chapter1"
raw_version = 1
spun_version = 1

with open("Scraper/text/chapter1_ocr_extracted.txt", "r", encoding="utf-8") as f:
    original_text = f.read()

output_mode = choose_output_mode("original chapter")
if output_mode == "audio":
    speak_text(original_text[:500])
else:
    print("\n📖 ORIGINAL CHAPTER:\n")
    print(original_text[:1000])

response = input("\n💬 Do you want to rewrite this chapter? (yes/no): ").strip().lower()
if response != "yes":
    print("✅ No changes requested. Saving original version.")
    store_text_version(
        chapter_id=chapter_id,
        text=original_text,
        source="ocr",
        stage="raw",
        version=raw_version
    )
    exit()

store_text_version(
    chapter_id=chapter_id,
    text=original_text,
    source="ocr",
    stage="raw",
    version=raw_version
)

while True:
    print("\n♻️ You can say or type 'exit' anytime to stop.")

    print("\n🧠 Provide your suggestion for rewriting:")
    user_suggestion = choose_input_mode()
    if user_suggestion.lower() == "exit":
        print("👋 Exiting the loop.")
        break

    spun_text = spin_text(original_text, user_suggestion=user_suggestion)

    output_mode = choose_output_mode("spun version")
    if output_mode == "audio":
        speak_text(spun_text[:500])
    else:
        print("\n📝 Spun Text Preview:\n")
        print(spun_text[:1000])

    with open(f"Scraper/text/{chapter_id}_spun_v{spun_version}.txt", "w", encoding="utf-8") as f:
        f.write(spun_text)

    store_text_version(
        chapter_id=chapter_id,
        text=spun_text,
        source="AI_writer",
        stage="spun",
        version=spun_version
    )

    print("\n📣 Provide feedback on the spun version:")
    feedback_text = choose_input_mode()
    if feedback_text.lower() == "exit":
        print("👋 Exiting the loop.")
        break

    full_id = f"{chapter_id}_spun_v{spun_version}"
    update_reward_and_feedback(full_id, feedback_text)

    print("\n🔍 Similar chapter suggestions based on your feedback:")
    search_similar_chapters(query=feedback_text)

    spun_version += 1

print("\n✅ Workflow completed successfully.")
