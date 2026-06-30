from telegram import Update
from telegram.ext import ContextTypes
from services.countdown import get_remaining_days
from services.ai import generate_ai_message


async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "countdown":
        days = get_remaining_days()

        text = generate_ai_message(days, context="callback")

        await query.edit_message_text(text)