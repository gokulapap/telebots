import telebot
from os import system
from time import sleep

#add bot api key
bot = telebot.TeleBot('xxxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxx')
global imgurl

@bot.message_handler(commands=['start'])
def welcome(message):
   bot.send_message(message.chat.id, "Welcome to Acrisius kamer bot!\nJust send an Image and text")

@bot.message_handler(commands=['owner'])
def welcome(message):
   bot.send_message(message.chat.id, "This bot was created by Gokul")

@bot.message_handler(commands=['help'])
def welcome(message):
   bot.send_message(message.chat.id, "send a photo and type top and bottom captions to add in two lines\nExample:\n\nfirst line here\nsecond line here\n\nIf you dont want top captions , just put top in first line and same for bottom")

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

   call = bot.send_message(message.chat.id, "Enter topline and bottomline captions in two lines")
   bot.register_next_step_handler(call, inputs_result)

def inputs_result(message):
 try:
   msg = message.text
   try:
     msg = msg.split("\n")
     if msg[0] == 'top':
       top = '%20'
     else:
       top = msg[0]
       top = top.split(" ")
       top = "%20".join(top)
     if msg[1] == 'bottom':
       bottom = '%20'
     else:
       bottom = msg[1]
       bottom = bottom.split(" ")
       bottom = "%20".join(bottom)
   except:
     top = msg
     top = top.split(" ")
     top = "%20".join(top)

     bottom = '%20'

   bot.send_message(message.chat.id, "Processing...")

   with open('img','r') as im:
     imgurl = im.readline()
   imgurl = imgurl.rstrip()

   system("wget 'https://docs-jojo.herokuapp.com/api/meme-gen?top={}&bottom={}&img={}' -O out.png".format(top,bottom,imgurl))
   file = open('out.png','rb')
   bot.send_photo(message.chat.id, file)
 except:
  bot.send_message(message.chat.id, "some error occured try again later")

bot.polling()
