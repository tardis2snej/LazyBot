import telebot
import time
from flask import Flask, request

server = Flask(__name__)
bot = telebot.TeleBot('986852722:AAHBNwKBZj3Brq5uk9l346Fn570cOI6dY3A')
bot.remove_webhook()
time.sleep(2)
bot.set_webhook(url="https://lazy-bot007.herokuapp.com/bot986852722:AAHBNwKBZj3Brq5uk9l346Fn570cOI6dY3A/")


@server.route("/", methods=['POST'])
def getMessage():
  r = request.get_json()
  if "message" in r.keys():
    chat_id = r["message"]["chat"]["id"]
    if "text" in r["message"]:
      text_mess = r["message"]["text"]
    else:
      bot.send_message(chat_id=chat_id, text="Какая то не понятная проблема", parse_mode='HTML')
      return "ok", 200

  if text_mess == '/start':
    bot.send_message(chat_id=chat_id, text="Привет WebHook")
    return "ok", 200


if __name__ == "main":
  server.run()