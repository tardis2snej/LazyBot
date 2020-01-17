import telebot

bot = telebot.TeleBot('986852722:AAHBNwKBZj3Brq5uk9l346Fn570cOI6dY3A')


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет!')


@bot.message_handler()
def answer(message):
    bot.send_message(message.chat.id, ':)')


bot.polling()