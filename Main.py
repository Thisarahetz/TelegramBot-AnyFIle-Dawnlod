
import telebot
import os
import time
#from dotenv import load_dotenv




#load_dotenv()

#bot_token = os.getenv('API_KEY')
bot_token=os.environ.get('API_KEY',"")

bot=telebot.TeleBot(token=bot_token,parse_mode=None)



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

while True:
    try:
        bot.polling(none_stop=True)
         #ConnectionError and ReadTimeout because of possible timout of the requests library
         #maybe there are others, therefore Exception
    except Exception:
       time.sleep(15)

#bot.polling()