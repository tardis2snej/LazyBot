# -*- coding: utf-8 -*-
import telebot
import os
import config
from flask import Flask, request

bot = telebot.TeleBot(config.TOKEN)

print("HELLO HUROKU")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Как насчет ленивого разговора?")


@bot.message_handler(content_types=['text'])
def send_text(message):
    if 'как дела' in message.text.lower():
        bot.send_message(message.chat.id, "Все отлично!")
    elif 'ты классный' in message.text.lower():
        bot.send_sticker(message.chat.id, 'CAADAgADMwIAArrAlQWc3UwCquHIDhYE')
    else:
        bot.send_message(message.chat.id, "Отличная погодка, не правда ли?")


# Проверим, есть ли переменная окружения Хероку
if "HEROKU" in list(os.environ.keys()):
    server = Flask(__name__)


    @server.route("/" + config.TOKEN, methods=['POST'])
    def getMessage():
        print("LET'S DO WEBHOOK")
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200


    @server.route("/")
    def webhook():
        print("INDEX PAGE")
        bot.remove_webhook()
        bot.set_webhook(bot.set_webhook(url="https://{}.herokuapp.com/{}".format(config.APP_NAME, config.TOKEN)))
        return "?", 200


    server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))
else:
    # если переменной окружения HEROKU нету, значит это запуск с машины разработчика.
    # Удаляем вебхук на всякий случай, и запускаем с обычным поллингом.
    bot.remove_webhook()
    bot.polling(none_stop=True)