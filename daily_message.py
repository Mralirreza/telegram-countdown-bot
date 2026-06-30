def send_message():
    days = get_remaining_days()

    text = f"⏳ شمارش معکوس:\n\n{days} روز تا ۱ مهر ۱۴۰۵ باقی مانده"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }

    response = requests.post(url, data=payload)

    print("STATUS CODE:", response.status_code)
    print("RESPONSE:", response.text)