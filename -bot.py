import logging
import os
import time
import telebot
from flask import Flask, request
import bot_setup

bot = telebot.TeleBot(bot_setup.get_token())
bot.remove_webhook()
time.sleep(2)
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

if "HEROKU" in list(os.environ.keys()):
    app = Flask(__name__)


    @app.route("/bot" + get_token(), methods=['POST'])
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


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет!')


@bot.message_handler()
def answer(message):
    bot.send_message(message.chat.id, ':)')


if not bot_setup.is_dev_run():
    bot.set_webhook(url="https://lazy-bot007.herokuapp.com/bot" + bot_setup.get_token())
    print("WEBHOOK SET")

bot_setup.start_bot(bot, __name__)






