from telegram import Update
from telegram.ext import ContextTypes
from services.countdown import get_remaining_days


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    days = get_remaining_days()

    text = f"⏳ تا ۱ مهر ۱۴۰۵\n\n{days} روز باقی مانده است."

    await update.message.reply_text(text)