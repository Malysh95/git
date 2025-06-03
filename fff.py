from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

QUESTION_TEXT = "Вопрос: 'Столица Франции?'"
OPTIONS = [("Париж", True), ("Берлин", False), ("Мадрид", False)]

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton(text=option[0], callback_data=str(i))]
        for i, option in enumerate(OPTIONS)
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(QUESTION_TEXT, reply_markup=reply_markup)

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    selected_index = int(query.data)
    is_correct = OPTIONS[selected_index][1]

    if is_correct:
        query.answer("Правильно!", show_alert=True)
    else:
        query.answer("Неправильно!", show_alert=True)

    query.edit_message_text(text="Спасибо за ответ!")

def main():
    updater = Updater("токен", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()