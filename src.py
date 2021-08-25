import os
import telebot
from dotenv import load_dotenv

#To load .env file
load_dotenv()

#To fetch API_KEY from .env file
API_KEY = os.getenv('API_KEY')

#Bot Creation
bot = telebot.TeleBot(API_KEY)

#Commands Handler
#Reply Message Handler
@bot.message_handler(commands=["Hey"])
def func_reply(msg):
        bot.reply_to(msg, "What's up")


def say_my_name(msg):
        return True

#Function Handler
@bot.message_handler(func=say_my_name)
def caller(msg):
        pass

#To check for Message repeatedly
bot.polling(none_stop=True,skip_pending=True)
