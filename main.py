from os import path
from urllib.request import urlopen
import telebot

bot = telebot.TeleBot("6552995612:AAGpPJPmKHJBKeSbzNJPxjxM3-8HDXa_rec") 

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, "سلاو,بەخیرهاتی بۆ بۆتی پایثۆن                                                                        ئەم بۆتە لەلایەن @B52_Plan_B                            دروستکراوە.")

@bot.message_handler(commands=["help"])
def send_help(message):
  bot.send_message(message.chat.id, "چۆن یارمەتیت بەدەم؟ بۆ هەر فیربونیک لە زمانەکانی پرۆگرامینگ ئەمانە داگرە /html + /python")
@bot.message_handler(commands=["python"])
def send_python(message):
  bot.send_message(message.chat.id, "لینکی کەنال بۆ فیربوون https://t.me/b52_plan بەهیوای سوود")
@bot.message_handler(commands=["html"])
def send_html(message):
  bot.send_message(message.chat.id, "لینکی کەنال بۆ فیربوون https://t.me/b52_plan بەهیوای سوود")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()

