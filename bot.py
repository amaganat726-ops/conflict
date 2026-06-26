import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# ВАШ ТОКЕН от @BotFather
TOKEN = "8961663653:AAFJi2ebXctwpEpLJ0r96R34IcWeIzln1I8"

# ССЫЛКА на ваше мини-приложение (GitHub Pages)
WEBAPP_URL = "https://amaganat726-ops.github.io/conflict/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🌀 Открыть карту конфликтов", web_app={"url": WEBAPP_URL})]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Нажмите кнопку, чтобы открыть карту конфликтов:",
        reply_markup=reply_markup
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("map", start))  # можно и /map
    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        webhook_url=None  # Render сам задаст URL
    )

if __name__ == "__main__":
    main()
