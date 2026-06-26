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
    # Создаём приложение с токеном
    app = Application.builder().token(TOKEN).build()

    # Регистрируем команды
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("map", start))  # чтобы можно было вызвать /map

    # Запускаем polling (опрос) — это самый надёжный способ для Render
    print("✅ Бот запущен и ожидает сообщения...")
    app.run_polling()

if __name__ == "__main__":
    main()
