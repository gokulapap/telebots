import telebot
import json
import requests

#add bot api key
bot = telebot.TeleBot("xxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxxx")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.send_message(message.chat.id, "Hello welcome to AI chat Bot")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
  req = message.text
  resp = requests.get('https://api.simsimi.net/v1/?text={}&lang=en&cf=true'.format(req))
  resp = json.loads(resp.text)
  bot.send_message(message.chat.id, '🤖 : '+resp['messages'][0]['response'])

bot.polling()
