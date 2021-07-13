import telebot
from os import system
import json
import requests as r
import random

#bot api key
bot = telebot.TeleBot("xxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxx")

@bot.message_handler(commands=['start'])
def handle_command(message):
    bot.reply_to(message, "Hello, Welcome to Tech News bot")

@bot.message_handler(commands=['help'])
def handle_command(message):
    bot.reply_to(message, "Type /getnews to get Latest news")

@bot.message_handler(commands=['author','owner'])
def handle_command(message):
    bot.reply_to(message, "* News api is created by Srivathsan \n* This bot is created By Gokul")

@bot.message_handler(commands=['getnews'])
def handle_command(message):
  try:
    a = r.get('https://dab8325046ba.ngrok.io/getNews/gokulap/e45PuaPjGseTyh7d4FGcJg')
    b = json.loads(a.text)

    i = random.randrange(188)

    result = ''
    author = b['response']['articles'][i]['Author']
    result = result + "Author:\n" + author
    result = result + '\n\n'
    url = b['response']['articles'][i]['Url']
    result = result + "URL:\n" + url
    result = result + '\n\n'

    bot.send_message(message.chat.id, result)

  except:
    bot.send_message(message.chat.id, "some error occured! Try again!")

# handle all messages, echo response back to users
@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
  pass
bot.polling()
