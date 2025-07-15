import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(groq_api_key=groq_api_key, model="llama3-8b-8192", temperature=0)

prompt = PromptTemplate.from_template("""
Analyze the following human feedback and return a reward score from 1 to 5:
1 = very bad, 5 = excellent.

Feedback:
"{feedback}"

Only return the number.
""")
chain = prompt | llm | StrOutputParser()

def feedback_to_reward_llm(feedback_text: str) -> int:
    try:
        score = chain.invoke({"feedback": feedback_text})
        return int(score.strip())
    except Exception as e:
        print(f"❌ LLM reward parsing failed: {e}")
        return 3

# Fallback rule-based


