import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# === Load environment variables ===
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# === Setup LLM ===
llm = ChatGroq(groq_api_key=groq_api_key, model="llama3-8b-8192", temperature=0.7)

# === Prompt Template for rewriting ===
prompt_template = ChatPromptTemplate.from_template("""
You are a helpful assistant.

Follow the instruction below to rewrite the chapter:

Instruction:
{user_instruction}

Chapter:
\"\"\"{chapter_text}\"\"\"
""")

# === Output parser ===
output_parser = StrOutputParser()

# === Main Rewrite Function ===
def spin_text(original_text: str, user_suggestion: str | None = None) -> str:
    if not user_suggestion or not user_suggestion.strip():
        print("ℹ️ No user suggestion given. Returning original text without spinning.")
        return original_text

    chain = prompt_template | llm | output_parser
    try:
        rewritten = chain.invoke({
            "chapter_text": original_text,
            "user_instruction": user_suggestion
        })
        return rewritten
    except Exception as e:
        print(f"❌ LLM failed to spin text: {e}")
        return original_text
