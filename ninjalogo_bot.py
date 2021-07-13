import telebot
from os import system

# Go to Botfather in Telegram and create api key
bot = telebot.TeleBot('xxxxxxx:xxxxxxxxxxxxxxxxxxxxx') #add your telegram bot api key

@bot.message_handler(commands=['start'])
def welcome(message):
  bot.send_message(message.chat.id, "Enter your name and you will get Ninjalogo with your name")

@bot.message_handler(commands=['owner'])
def welcome(message):
  bot.send_message(message.chat.id, "This bot was created by Gokul")

@bot.message_handler(func=lambda message: True)
def input(message):
 try:
  name = message.text
  if " " in name:
    name = name.split(" ")
    mname = "%20".join(name)
    fname = "".join(name)
    system('wget https://docs-jojo.herokuapp.com/api/gaming?text={} -O {}.jpg'.format(mname, fname))
    image = open('{}.jpg'.format(fname), 'rb')
    bot.send_photo(message.chat.id, image)
    system('rm {}.jpg'.format(fname))
  else:
    system('wget https://docs-jojo.herokuapp.com/api/gaming?text={} -O {}.jpg'.format(name,name))
    image = open('{}.jpg'.format(name), 'rb')
    bot.send_photo(message.chat.id, image)
    system('rm {}.jpg'.format(name))
 except:
  bot.send_message(message.chat.id, "some error ocuured try again later !")

bot.polling()
