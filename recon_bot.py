import telebot
from os import system

#add bot api key
bot = telebot.TeleBot("1780974722:AAH27FxV7AWqkIFZ71A1UBiWzKnl8-cwGLQ")

@bot.message_handler(commands=['start'])
def handle_command(message):
    bot.reply_to(message, "Hello, welcome to Recon Bot!\n\nType /help for help \nType /author to see author name \n\n1)Type /dnscan (target.com)\n2)Type /subdomain (target.com)\n\nReplace target.com with your target ")

@bot.message_handler(commands=['help'])
def handle_command(message):
    bot.reply_to(message, "Recon_bot help: \n\n1)Type /dnscan (target.com) for dnscan \n2)Type /subdomain (target.com) to enumerate subdomains \n\nReplace target.com with your target")

@bot.message_handler(commands=['author','owner'])
def handle_command(message):
    bot.reply_to(message, "This bot is created By Gokul")

@bot.message_handler(commands=['dnscan'])
def handle_command(message):
  try:
    msg = message.text
    if msg == '/dnscan':
     bot.send_message(message.chat.id, "Empty command found Try with arguments")
     raise Exception("Empty command found")
    a = msg.split(" ")
    if len(a) < 2:
      bot.send_message(message.chat.id, "Invalid command try /help and Enter correctly")
      bot.polling()
    msg = a[1]
    msg = msg.lower()
    bot.send_message(message.chat.id,"wait patiently...")
    system("bash test.sh {} | tee {}.dns".format(msg,msg))
    f = open("{}.dns".format(msg),"r")
    b = f.readlines()
    c = ''
    for i in range(len(b)):
      c = c + b[i]
    bot.send_message(message.chat.id, c)
  except:
   bot.send_message(message.chat.id,"oops some error has occured ! Try again later")

@bot.message_handler(commands=['subdomain'])
def handle_command(message):
  try:
    msg = message.text
    if msg == '/subdomain':
     bot.send_message(message.chat.id, "Empty command found Try with arguments")
     raise Exception("Empty command found")
    a = msg.split(" ")
    if len(a) < 2:
      bot.send_message(message.chat.id, "Invalid command try /help and Enter correctly")
      bot.polling()
    msg = a[1]
    msg = msg.lower()
    msg = msg.replace(" ","")
    msg = msg.replace("https://","")
    msg = msg.replace("http://","")
    msg = msg.replace("Http://","")
    msg = msg.replace("Https://","")
    if '.' in msg:
                try:
                  bot.send_message(message.chat.id, "Wait Patiently...")
                  print(msg + '\n')
                  system("curl -s 'https://crt.sh/?q={}' | grep '<TD>' | grep {} | cut -d '>' -f2 | cut -d '<' -f1 | sort -u | sed '/^*/d' | tee -a {}.txt".format(msg,msg,msg))
                  system("curl -s 'https://rapiddns.io/subdomain/{}#result' | grep '<td><a' | cut -d '\"' -f 2 | grep http | cut -d '/' -f3 | sed '/^*/d | tee -a {}.txt".format(msg,msg))
                  system("curl -s 'https://jldc.me/anubis/subdomains/{}' | grep -Po '((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+' | cut -d '/' -f3 | sort -u | tee -a {}.txt".format(msg,msg))
                  system("sort {}.txt | uniq | sed '/^*/d' | tee -a {}".format(msg,msg))
                  f = open('{}'.format(msg),'r')
                  a = f.readlines()
                  b = ''
                  c = ''
                  if len(a) == 0:
                    bot.send_message(message.chat.id, "Invalid domain or subdomains not found!")
                  elif len(a) > 500 or len(a) > 1000:
                    for j in range(500):
                      b = b+a[j]
                    bot.send_message(message.chat.id, b)
                    for k in range(500,len(a)):
                      c = c+a[k]
                    bot.send_message(message.chat.id, c)
                  else:
                    bot.send_message(message.chat.id, "{} subdomains found for {}".format(len(a), msg))
                    for i in range(len(a)):
                      b = b + a[i]
                    f.close()
                    bot.send_message(message.chat.id, b)
                except:
                  bot.send_message(message.chat.id, "oops! some error occured! Try again later")
    else:
                bot.send_message(message.chat.id, "Not an valid domain")

  except:
    bot.send_message(message.chat.id, "oops some error occured ! Try again later")

# handle all messages, echo response back to users
@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
  bot.send_message(message.chat.id, "see the /help command and try again")

bot.polling()
