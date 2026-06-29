from telegram import Update
from telegram.ext import ContextTypes
from services.countdown import get_remaining_days

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "countdown":
        days = get_remaining_days()
        await query.edit_message_text(
            f"⏳ تا ۱ مهر ۱۴۰۵\n\n{days} روز باقی مانده است."
        )