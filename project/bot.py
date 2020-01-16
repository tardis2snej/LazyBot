# -*- coding: utf-8 -*-
import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Как насчет ленивого разговора?")


@bot.message_handler(content_types=['text'])
def send_text(message):
    if 'как дела' in message.text.lower():
        bot.send_message(message.chat.id, "Все отлично!")
    elif 'ты классный' in message.text.lower():
        bot.send_sticker(message.chat.id, 'CAADAgADMwIAArrAlQWc3UwCquHIDhYE')


@bot.message_handler(content_types=['sticker'])
def display(message):
    print(message)


if __name__ == '__main__':
    bot.infinity_polling()