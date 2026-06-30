import os
import requests
import random
from dotenv import load_dotenv
from services.countdown import get_remaining_days

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


# 🧠 "AI STYLE ENGINE"
def ai_generate_message(days: int) -> str:

    tones = [
        "casual",
        "motivational",
        "dramatic",
        "minimal",
        "friendly"
    ]

    tone = random.choice(tones)

    # 🔥 Context understanding layer
    if days <= 5:
        context = "critical_final_stage"
    elif days <= 15:
        context = "urgent_stage"
    elif days <= 30:
        context = "active_stage"
    else:
        context = "early_stage"

    # 🧠 AI-like generation logic
    if context == "critical_final_stage":
        base = [
            f"😱 فقط {days} روز مونده... همه‌چیز داره تموم میشه!",
            f"🚨 لحظه‌های آخره... {days} روز باقی مونده!",
            f"🔥 نزدیک‌ترین حالت ممکن... {days} روز!"
        ]

    elif context == "urgent_stage":
        base = [
            f"⚠️ داریم نزدیک می‌شیم... {days} روز مونده",
            f"⏳ زمان داره جدی میشه... فقط {days} روز",
            f"🎯 تقریباً رسیدیم... {days} روز باقی مونده"
        ]

    elif context == "active_stage":
        base = [
            f"🚀 مسیر ادامه داره... {days} روز تا هدف",
            f"📅 هنوز در حرکتیم... {days} روز باقی مونده",
            f"🔥 پیشرفت ادامه داره ({days} روز)"
        ]

    else:
        base = [
            f"🌱 مسیر تازه شروع شده... {days} روز باقی مونده",
            f"⏳ هنوز زمان داریم... {days} روز تا هدف",
            f"📊 فعلاً در فاز اولیه هستیم ({days} روز)"
        ]

    message = random.choice(base)

    # 🎭 tone enhancer (AI-like personality layer)
    if tone == "motivational":
        message += " 💪 ادامه بده!"
    elif tone == "dramatic":
        message += " 😳"
    elif tone == "friendly":
        message += " 😊"
    elif tone == "minimal":
        message = f"{days} روز باقی مانده"
    else:
        message += ""

    return message


def send_message():
    days = get_remaining_days()

    text = ai_generate_message(days)

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }

    response = requests.post(url, data=payload)

    print("STATUS CODE:", response.status_code)
    print("RESPONSE:", response.text)


if __name__ == "__main__":
    send_message()