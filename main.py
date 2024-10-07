import telebot
import requests

TOKEN = '7562461923:AAEnwHGdqtsq8cdDh2XhnTpylurvAyyOGPA'

bot = telebot.TeleBot(TOKEN)


def greet_user():
    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, "Добрый день. Как вас зовут?")
    
    @bot.message_handler(func=lambda message: True)
    def collect_name(message):
        global username
        username = message.text
        bot.send_message(message.chat.id, f"Здравствуйте, {username}! Курс доллара сегодня ... (получение данных)")

        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
       
        response = requests.get(url).json()
      
        rate = response['Valute']['USD']['Value']
      
        bot.send_message(message.chat.id, f"Курс доллара сегодня {rate} рублей.")


greet_user()


bot.infinity_polling()
