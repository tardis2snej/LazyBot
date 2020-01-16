# -*- coding: utf-8 -*-
import telebot
import config
import os
from flask import Flask, request

bot = telebot.TeleBot(config.TOKEN)
server = Flask(__name__)


@server.route("/" + config.TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route('/', methods=["GET"])
def index():
    bot.remove_webhook()
    bot.set_webhook(url="https://{}.herokuapp.com/{}".format(config.APP_NAME, config.TOKEN))
    return "Hello from Heroku!", 200


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
        bot.send_message("Отличная погодка, не правда ли?")


if __name__ == '__main__':
    bot.infinity_polling()


server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
server = Flask(__name__)