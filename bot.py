import time

import telebot
import bot_setup

bot = telebot.TeleBot(bot_setup.get_token())
bot.remove_webhook()
time.sleep(2)
bot_setup.setup(bot)


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






