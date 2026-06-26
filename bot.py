import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# ----- ВАШ ТОКЕН -----
TOKEN = "8961663653:AAFJi2ebXctwpEpLJ0r96R34IcWeIzln1I8"

# ----- ССЫЛКА НА МИНИ-ПРИЛОЖЕНИЕ (GitHub Pages) -----
WEBAPP_URL = "https://amaganat726-ops.github.io/conflict/"

# ----- АДРЕС ВАШЕГО СЕРВИСА НА RENDER (для вебхука) -----
RENDER_URL = "https://conflict-ypni.onrender.com"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_type = update.effective_chat.type

    # Для личных чатов – кнопка web_app
    if chat_type == "private":
        keyboard = [[InlineKeyboardButton("🌀 Открыть карту конфликтов", web_app={"url": WEBAPP_URL})]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            "Нажмите кнопку, чтобы открыть карту конфликтов:",
            reply_markup=reply_markup
        )
    else:
        # Для групп – обычная кнопка с URL (откроется в браузере)
        keyboard = [[InlineKeyboardButton("🌀 Открыть карту конфликтов", url=WEBAPP_URL)]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            "Нажмите кнопку, чтобы открыть карту конфликтов (откроется в браузере):",
            reply_markup=reply_markup
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("map", start))

    port = int(os.environ.get("PORT", 10000))

    # Запускаем вебхук
    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        webhook_url=RENDER_URL,
        close_loop=False
    )

if __name__ == "__main__":
    main()
