import os
import requests
from dotenv import load_dotenv
from openai import OpenAI
from services.countdown import get_remaining_days

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_ai_message(days: int) -> str:
    prompt = f"""
You are a motivational countdown assistant.

We have {days} days left until a deadline (1 Mehr 1405).

Generate a SHORT, natural, human-like Telegram message in Persian.

Rules:
- max 2 sentences
- emotional but not too long
- vary tone each time
- do NOT repeat previous styles
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


def send_message():
    days = get_remaining_days()

    text = generate_ai_message(days)

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }

    response = requests.post(url, data=payload)

    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)


if __name__ == "__main__":
    send_message()