import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# ----- ВАШ ТОКЕН -----
TOKEN = "8961638653:AAFJ2ebXctwpEpLJ0r96R34IcWeI2lniI8"

# ----- ССЫЛКА НА МИНИ-ПРИЛОЖЕНИЕ (GitHub Pages) -----
WEBAPP_URL = "https://amaganat726-ops.github.io/conflict_/"

# ----- АДРЕС ВАШЕГО СЕРВИСА НА RENDER -----
# Например: https://conflict-ypni.onrender.com
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

    # Устанавливаем вебхук при старте
    async def setup_webhook():
        await app.bot.set_webhook(url=RENDER_URL)
        print(f"✅ Webhook установлен на {RENDER_URL}")

    # Запускаем установку вебхука (создаёт новый цикл)
    asyncio.run(setup_webhook())

    # Запускаем вебхук-сервер
    port = int(os.environ.get("PORT", 10000))
    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        webhook_url=RENDER_URL
    )

if __name__ == "__main__":
    main()
