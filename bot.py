import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# ----- ВСТАВЬТЕ СВОЙ ТОКЕН (полученный от @BotFather) -----
TOKEN = "8961663653:AAFJi2ebXctwpEpLJ0r96R34IcWeIzln1I8"

# ----- ССЫЛКА НА ВАШЕ МИНИ-ПРИЛОЖЕНИЕ (GitHub Pages) -----
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
    app.add_handler(CommandHandler("map", start))

    # Получаем порт из переменной окружения (Render задаёт PORT)
    port = int(os.environ.get("PORT", 10000))

    # Получаем URL сервиса из переменной окружения WEBHOOK_URL (обязательно задайте её в настройках Render)
    webhook_url = os.environ.get("WEBHOOK_URL")
    if not webhook_url:
        # Если не задана, используем заглушку (но лучше всегда задавать)
        webhook_url = "https://ваш_сервис.onrender.com"

    # Запускаем вебхук
    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        webhook_url=webhook_url
    )

if __name__ == "__main__":
    main()
