import telebot
from os import system

bot = telebot.TeleBot('xxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxx')

@bot.message_handler(commands=['start'])
def welcome(message):
   bot.reply_to(message, "welcome to Image to text telebot!")

@bot.message_handler(commands=['info'])
def info(message):
   bot.reply_to(message, "Send an image and i will return the text extracted from that image!")

@bot.message_handler(content_types = ['photo'])
def imgtotxt(message):
   fileid = message.photo[0].file_id
   bot.send_chat_action(message.chat.id, 'upload_photo')
   file = bot.get_file(fileid)
   filepath = file.file_path
   download = bot.download_file(filepath)
   with open("img.png", 'wb') as new_file:
     new_file.write(download)
   call = bot.send_message(message.chat.id, "photo received! Extracting the text from the image ...")
   bot.register_next_step_handler(call, processe)

def processe(message):
  system("tesseract img.png out")
  f = open("out.txt","r")
  text = f.read()
  f.close()
  bot.send_message(message.chat.id, "Retrieved Text is: ") 
  bot.send_message(message.chat.id, text)

print("polling...")
bot.polling()

