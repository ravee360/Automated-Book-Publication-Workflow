from agents.llm_writer import spin_text
from db.store_chapters import store_text_version
from db.update_metadata import update_reward_and_feedback
from utils.voice_interface import get_voice_input, speak_text, choose_input_mode, choose_output_mode
from utils.semantic_search import search_similar_chapters

# === Config ===
chapter_id = "chapter1"
raw_version = 1
spun_version = 1

# === Step 1: Load and Show Original Text ===
with open("Scraper/text/chapter1_ocr_extracted.txt", "r", encoding="utf-8") as f:
    original_text = f.read()

# === Step 2: Let User Choose to View or Listen ===
output_mode = choose_output_mode("original chapter")
if output_mode == "audio":
    speak_text(original_text[:500])
else:
    print("\n📖 ORIGINAL CHAPTER:\n")
    print(original_text[:1000])

# === Step 3: Ask if user wants to give feedback ===
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

# === Step 4: Store original version ===
store_text_version(
    chapter_id=chapter_id,
    text=original_text,
    source="ocr",
    stage="raw",
    version=raw_version
)

# === Step 5: Loop for continuous feedback/spinning ===
while True:
    print("\n♻️ You can say or type 'exit' anytime to stop.")

    # === Get User Suggestion ===
    print("\n🧠 Provide your suggestion for rewriting:")
    user_suggestion = choose_input_mode()
    if user_suggestion.lower() == "exit":
        print("👋 Exiting the loop.")
        break

    # === Spin the text with LLM ===
    spun_text = spin_text(original_text, user_suggestion=user_suggestion)

    # === Output spun version ===
    output_mode = choose_output_mode("spun version")
    if output_mode == "audio":
        speak_text(spun_text[:500])
    else:
        print("\n📝 Spun Text Preview:\n")
        print(spun_text[:1000])

    # Save to file for inspection
    with open(f"Scraper/text/{chapter_id}_spun_v{spun_version}.txt", "w", encoding="utf-8") as f:
        f.write(spun_text)

    # === Store spun version ===
    store_text_version(
        chapter_id=chapter_id,
        text=spun_text,
        source="AI_writer",
        stage="spun",
        version=spun_version
    )

    # === Final Feedback ===
    print("\n📣 Provide feedback on the spun version:")
    feedback_text = choose_input_mode()
    if feedback_text.lower() == "exit":
        print("👋 Exiting the loop.")
        break

    full_id = f"{chapter_id}_spun_v{spun_version}"
    update_reward_and_feedback(full_id, feedback_text)

    # === Optional: Semantic Search ===
    print("\n🔍 Similar chapter suggestions based on your feedback:")
    search_similar_chapters(query=feedback_text)

    spun_version += 1

print("\n✅ Workflow completed successfully.")
