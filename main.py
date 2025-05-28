
import os
import telebot
from flask import Flask, request

API_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "سلام! برای دانلود اپلیکیشن مستر مکانیک روی لینک زیر بزن:
https://your-domain.com/mrmichanic.apk")

@server.route(f"/{API_TOKEN}", methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "OK", 200

@server.route("/")
def index():
    return "MrMichanic Bot is running!"

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"https://your-domain.com/{API_TOKEN}")
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
