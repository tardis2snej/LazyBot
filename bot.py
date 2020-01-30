import os
import time
import telebot
from flask import Flask, request
import logging

if "TOKEN" in list(os.environ.keys()):
    token = os.environ.get('TOKEN')
    isDevRun = False
else:
    import config
    token = config.TOKEN
    isDevRun = True

bot = telebot.TeleBot(token)

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot.remove_webhook()
time.sleep(2)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет!')


@bot.message_handler()
def answer(message):
    bot.send_message(message.chat.id, ':)')


# starting bot
if not isDevRun:
    bot.set_webhook(url="https://lazy-bot007.herokuapp.com/bot" + token)
    print("WEBHOOK SET")
    app = Flask(__name__)


    @app.route("/bot" + token, methods=['POST'])
    def get_message():
        print("POST METHOD")
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200


    @app.route("/", methods=['GET'])
    def index_page():
        print("GET METHOD")
        return "!", 200


    app.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
else:
    print("DEV RUN")
    bot.polling()
