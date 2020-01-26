import os
import telebot
import logging
import time
from flask import Flask, request


def get_token():
    if "HEROKU" in list(os.environ.keys()):
        token = os.environ.get('token')
    else:
        import config
        token = config.TOKEN
    return token


def setup(bot):
    logger = telebot.logger
    telebot.logger.setLevel(logging.INFO)

    bot.remove_webhook()
    time.sleep(2)


def start_bot(bot, name):
    if "HEROKU" in list(os.environ.keys()):
        bot.set_webhook(url="https://lazy-bot007.herokuapp.com/bot" + get_token())
        print("WEBHOOK SET")

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
        return app
    else:
        print("DEV RUN")
        bot.polling()
        return 0

