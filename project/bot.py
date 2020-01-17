# -*- coding: utf-8 -*-
from time import sleep

import telebot
import os
import config
from flask import Flask, request

bot = telebot.TeleBot(config.TOKEN)
# PORT = int(os.environ.get('PORT', '80'))
# print("PORT IS", PORT)


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
    print("HEROKU STARTING FLASK")
    app = Flask(__name__)
    print("FLASK RUNNING")
    bot.remove_webhook()
    sleep(1)
    bot.set_webhook(url="https://{}.herokuapp.com/bot{}".format(config.APP_NAME, config.TOKEN))
    print("WEBHOOK SET")

    @app.route("/bot{}".format(config.TOKEN), methods=['POST'])
    def get_message():
        print("LET'S DO UPDATE")
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200


    @app.route("/")
    def webhook():
        print("INDEX PAGE")
        return ".", 200

    # if __name__ == '__main__':
    print("START SERVER RUN")
        # server.run(host="0.0.0.0", port=PORT)
    app.run(threaded=True)
    print("END SERVER RUN")
else:
    # если переменной окружения HEROKU нету, значит это запуск с машины разработчика.
    # Удаляем вебхук на всякий случай, и запускаем с обычным поллингом.
    print("LONG POOLING")
    bot.polling(none_stop=True)
