import telebot
from os import system
from time import sleep

#add bot api key
bot = telebot.TeleBot('xxxxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxx')
global imgurl

@bot.message_handler(commands=['start'])
def welcome(message):
   bot.send_message(message.chat.id, "Welcome to Funny captcha creator bot with images")

@bot.message_handler(commands=['owner'])
def welcome(message):
   bot.send_message(message.chat.id, "This bot was created by Gokul")

@bot.message_handler(commands=['help'])
def welcome(message):
   bot.send_message(message.chat.id, "send a photo and username")

@bot.message_handler(content_types = ['photo'])
def send_document(message):
   fileid = message.photo[0].file_id
   bot.send_message(message.chat.id, "Your photo received..please wait..")
   file = bot.get_file(fileid)
   filepath = file.file_path
   download = bot.download_file(filepath)
   with open("meme.jpg", 'wb') as new_file:
     new_file.write(download)
   system("curl http://transfer.sh --upload-file meme.jpg > img")

   call = bot.send_message(message.chat.id, "Enter username")
   bot.register_next_step_handler(call, inputs_result)

def inputs_result(message):
   msg = message.text
   try:
    msg = msg.split(" ")
    msg = "%20".join(msg)
   except:
    pass

   bot.send_message(message.chat.id, "Processing...")

   with open('img','r') as im:
     imgurl = im.readline()
   imgurl = imgurl.rstrip()

   system("wget 'https://nekobot.xyz/api/imagegen?type=captcha&url={}&username={}&raw=1' -O out.png".format(imgurl,msg))
   file = open('out.png','rb')
   bot.send_photo(message.chat.id, file)

bot.polling()
