from telegram import Update
from telegram.ext import ContextTypes
from services.countdown import get_remaining_days
from services.ai import generate_ai_message


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    days = get_remaining_days()

    text = generate_ai_message(days, context="start")

    await update.message.reply_text(text)