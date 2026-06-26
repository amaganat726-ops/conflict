import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# ----- ВАШ ТОКЕН (убедитесь, что он правильный) -----
TOKEN = "8961638653:AAFJ2ebXctwpEpLJ0r96R34IcWeI2lniI8"

# ----- ССЫЛКА НА ВАШЕ МИНИ-ПРИЛОЖЕНИЕ (GitHub Pages) -----
WEBAPP_URL = "https://amaganat726-ops.github.io/conflict_/"

# ----- АДРЕС ВАШЕГО СЕРВИСА НА RENDER -----
RENDER_URL = "https://conflict-ypni.onrender.com"

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

    # Получаем порт из переменной окружения
    port = int(os.environ.get("PORT", 10000))

    # Запускаем вебхук с параметром close_loop=False
    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        webhook_url=RENDER_URL,
        close_loop=False  # <-- ЭТО ГЛАВНОЕ ИЗМЕНЕНИЕ
    )

if __name__ == "__main__":
    main()
