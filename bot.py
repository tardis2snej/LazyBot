import telebot
import bot_setup

bot = telebot.TeleBot(bot_setup.get_token())
bot_setup.setup(bot)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет!')


@bot.message_handler()
def answer(message):
    bot.send_message(message.chat.id, ':)')


bot_setup.start_bot(bot, __name__)






