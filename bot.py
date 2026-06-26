import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# ----- ВАШ ТОКЕН -----
TOKEN = "8961663653:AAFJi2ebXctwpEpLJ0r96R34IcWeIzln1I8"

# ----- ССЫЛКА НА МИНИ-ПРИЛОЖЕНИЕ (GitHub Pages) -----
WEBAPP_URL = "https://amaganat726-ops.github.io/conflict/"

# ----- АДРЕС ВАШЕГО СЕРВИСА НА RENDER -----
# Например: https://conflict-ypni.onrender.com
RENDER_URL = "https://ваш_сервис.onrender.com"   # <-- замените на свой

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

    # Устанавливаем вебхук при старте
    async def setup_webhook():
        webhook_url = RENDER_URL  # можно также брать из переменной окружения
        await app.bot.set_webhook(url=webhook_url)
        print(f"✅ Webhook установлен на {webhook_url}")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(setup_webhook())

    # Запускаем вебхук-сервер
    port = int(os.environ.get("PORT", 10000))
    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        webhook_url=RENDER_URL  # этот параметр нужен для проверки, но фактически вебхук уже установлен
    )

if __name__ == "__main__":
    main()
