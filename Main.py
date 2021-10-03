
import telebot
import os
import time
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(token)



@bot.message_handler(commands=["start"])
def sendDocument(message):
    bot.reply_to(message,"Enter Link")
    
   #bot.send_document(message.chat.id,"https://github.com/karipov/atlink/archive/refs/heads/master.zip","dwnlodgit")
    
    #print(bot.get_updates)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_document(message.chat.id,message.text,"dawnlod")


#@bot.message_handler(commands=["sendPhoto"])
#def send_message(message):
#    bot.reply_to(message,"Helloworkd")

# while True:
#     try:
#         bot.polling(none_stop=True)
#          #ConnectionError and ReadTimeout because of possible timout of the requests library
#          #maybe there are others, therefore Exception
#     except Exception:
#        time.sleep(15)

def main():
    bot.polling()

if __name__ == '__main__':
    main()