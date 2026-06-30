import random
import os
import requests
from dotenv import load_dotenv
from services.countdown import get_remaining_days

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message():
    days = get_remaining_days()

    messages = [
        f"⏳ فقط {days} روز تا ۱ مهر ۱۴۰۵ باقی مانده!",
        f"🔥 شمارش ادامه دارد... {days} روز باقی مانده!",
        f"🚀 نزدیک‌تر شدیم! فقط {days} روز!",
        f"😱 زمان داره می‌گذره... {days} روز مونده!",
        f"🎯 هدف نزدیکه! {days} روز باقی مانده!"
    ]

    text = random.choice(messages)

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