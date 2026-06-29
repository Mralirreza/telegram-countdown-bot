from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "⏳ چند روز تا ۱ مهر ۱۴۰۵؟",
                callback_data="countdown"
            )
        ]
    ]
    return InlineKeyboardMarkup(keyboard)