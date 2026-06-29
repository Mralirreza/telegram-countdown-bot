import random
import requests
from datetime import date
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

TARGET_DATE = date(2026, 9, 23)

messages = [
    "🔥 یه روز دیگه گذشت، نزدیک‌تر شدی!",
    "⏳ زمان در حال کاهشه...",
    "💪 ادامه بده، کم مونده!",
    "🚀 هر روز یه قدم جلوتر",
    "🌱 رشد یعنی ادامه دادن"
]

def get_days():
    return (TARGET_DATE - date.today()).days


def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})


if __name__ == "__main__":
    days = get_days()
    msg = random.choice(messages)

    final_text = f"""
⏳ شمارش معکوس

📅 {days} روز باقی مانده

{msg}
"""

    send_message(final_text)