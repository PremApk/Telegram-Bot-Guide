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

#Auto Message Handler
@bot.message_handler(commands=["JamesCameron", "jamescameron", "james", "cameron", "James", "JAMES", "Cameron"])
def func_greet(msg):
        bot.send_message(msg.chat.id, "James Cameron Filmography🎬\n\n\n"
                                      "1982  Piranha II: The Spawning\n\n"
                                      "1984  [The Terminator](https://t\.me/c/1343671235/24641)\n\n"
                                      "1986  [Aliens](https://t\.me/c/1343671235/24586)\n\n"
                                      "1989  [The Abyss](https://t\.me/c/1343671235/24587)\n\n"
                                      "1991  [Terminator 2: Judgment Day](https://t\.me/c/1343671235/24588)\n\n"
                                      "1994  [True Lies](https://t\.me/c/1343671235/24589)\n\n"
                                      "1997  [Titanic](https://t\.me/c/1343671235/24590)\n\n"
                                      "2003  [Ghosts of the Abyss](https://t\.me/c/1343671235/24591)\n\n"
                                      "2005  [Aliens of the Deep](https://t\.me/c/1343671235/24592)\n\n"
                                      "2009  [Avatar](https://t\.me/c/1343671235/24593)", parse_mode="MarkdownV2")

def say_my_name(msg):
        request = msg.text.split()
        print(request)
        if("Apk" in request):

                return True
        return False

#Function Handler
@bot.message_handler(func=say_my_name)
def caller(msg):
        pass

#To check for Message repeatedly
bot.polling(none_stop=True,skip_pending=True)
