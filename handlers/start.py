from telegram import Update
from telegram.ext import ContextTypes
from keyboards.main_keyboard import main_keyboard

print("START HANDLER LOADED")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 ربات شمارش معکوس\n\nیکی از گزینه‌ها را انتخاب کن:",
        reply_markup=main_keyboard()
    )