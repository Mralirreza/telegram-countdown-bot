import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_ai_message(days: int, context: str = "start") -> str:
    prompt = f"""
You are a Telegram countdown assistant.

Context: {context}
Days left: {days}

Rules:
- short (max 2 sentences)
- Persian language
- natural human tone
- emotional but not repetitive
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content