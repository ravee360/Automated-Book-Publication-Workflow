# 🚀 Automated-Book-Publication

It is a voice-interactive tool that takes raw chapter text (from OCR or scraped sources), lets users refine it using voice/text prompts, and rewrites it using an LLM. It stores multiple versions, allows semantic feedback search, and supports voice interaction throughout.

---
## Video Link:  https://youtu.be/Sz6HU21VGME  {Listen it at 1.5x}


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
| Data Source          | Playwright + Pytesseract      |

---

## 📂 Folder Structure
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


## 📂 Folder Structure

Servo-Nerve/
│
├── Scraper/
│ ├── ocr/
│ │ └── images/ # Raw scanned pages (optional)
│ └── text/
│ ├── chapter1_ocr_extracted.txt # Input used by main.py
│ └── chapter1_spun.txt # AI-modified version
│
├── agents/
│ └── llm_writer.py
│
├── db/
│ ├── store_chapters.py
│ └── update_metadata.py
│
├── utils/
│ ├── voice_interface.py
│ └── semantic_search.py
│
├── main.py
├── .env
└── requirements.txt

## ▶️ How to Run

1. **Clone the repo**

```bash
git clone https://github.com/your-username/Servo-Nerve.git
cd Servo-Nerve
python -m venv venv
venv\Scripts\activate    # On Windows

pip install -r requirements.txt
#### create .env
GROQ_API_KEY="<YOUR API KEY >

Run the app

bash
python main.py




