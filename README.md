# 🚀 Servo-Nerve

**Servo-Nerve** is a voice-interactive tool that takes raw chapter text (from OCR or scraped sources), lets users refine it using voice/text prompts, and rewrites it using an LLM. It stores multiple versions, allows semantic feedback search, and supports voice interaction throughout.

---

## 📦 Features

- 📄 OCR/Scraped text ingestion (via custom Scraper)
- 🔊 Voice + text input for chapter suggestions
- 🧠 LLM-powered rewriting (Groq + LangChain)
- 🗂️ Version tracking using ChromaDB
- 📢 Output via audio (gTTS + pygame) or terminal
- 🔍 Semantic search on human feedback
- 📊 Feedback scoring (rule-based + LLM)

---

## 🛠️ Tech Stack

| Feature               | Tool/Library                 |
|----------------------|------------------------------|
| Text Rewriting       | LangChain + Groq             |
| Prompt Handling      | LangChain Core Templates     |
| Semantic DB          | ChromaDB                     |
| Voice Input          | SpeechRecognition            |
| Text-to-Speech       | gTTS + pygame                |
| Feedback Scoring     | Custom + LLM (LLaMA3)        |
| Environment          | python-dotenv                |
| Data Source          | Local OCR or `Scraper/`      |

---

## 📂 Folder Structure

