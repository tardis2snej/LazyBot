import os
import time

import telebot
from flask import Flask, request
import logging

bot = telebot.TeleBot('986852722:AAHBNwKBZj3Brq5uk9l346Fn570cOI6dY3A')

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot.remove_webhook()
time.sleep(2)
bot.set_webhook(url="https://lazy-bot007.herokuapp.com/bot986852722:AAHBNwKBZj3Brq5uk9l346Fn570cOI6dY3A")
print("WEBHOOK SET")


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет!')


@bot.message_handler()
def answer(message):
    bot.send_message(message.chat.id, ':)')


app = Flask(__name__)


@app.route("/bot986852722:AAHBNwKBZj3Brq5uk9l346Fn570cOI6dY3A", methods=['POST'])
def get_message():
    print("POST METHOD")
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return 200


@app.route("/", methods=['GET'])
def index_page():
    print("GET METHOD")
    return "!", 200


print("BEFORE APP.RUN")
app.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
print("AFTER APP.RUN")
