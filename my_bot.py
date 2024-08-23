from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Вставьте свой токен сюда
TOKEN = '5519262335:AAGfd2b8Lu43SbncFbgDo80cO-8pAp7OXJw'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot.')

def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
