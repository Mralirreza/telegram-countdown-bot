from telegram import Update
from telegram.ext import ContextTypes
from telegram.error import BadRequest
from services.countdown import get_remaining_days

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "countdown":
        days = get_remaining_days()

        text = f"⏳ تا ۱ مهر ۱۴۰۵\n\n{days} روز باقی مانده است."

        try:
            await query.edit_message_text(text)
        except BadRequest as e:
            if "Message is not modified" not in str(e):
                raise