import logging
import os

import requests
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update: Update, context: telegram.ext.CallbackContext):
    update.message.reply_text("Добрый день. Как вас зовут?")


def greet(update: Update, context: telegram.ext.CallbackContext):
    name = update.message.text
    update.message.reply_text(f"Рад знакомству, {name}!")


def get_currency_rate(update: Update, context: telegram.ext.CallbackContext):
    api_key = dc975d9ede914d129ab5b961bf732f1d
    base_url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}&symbols=USD"
    response = requests.get(base_url)
    rate = response.json()['rates']['USD']
    update.message.reply_text(f"Курс доллара сегодня {rate} рублей.")


def main():
    updater = Updater(os.environ.get('TELEGRAM_TOKEN'), use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, greet))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, get_currency_rate))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
