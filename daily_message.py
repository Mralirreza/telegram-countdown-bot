import os
import requests
from dotenv import load_dotenv
from services.countdown import get_remaining_days

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message():
    days = get_remaining_days()

    text = f"⏳ شمارش معکوس:\n\n{days} روز تا ۱ مهر ۱۴۰۵ باقی مانده"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }

    requests.post(url, data=payload)

if __name__ == "__main__":
    send_message()