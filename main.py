# [IMPORT]
import telebot
from telebot import types
from KEY import API_KEY
from threading import Thread
from CoreSystem import CreateQR

# [CODE]
bot = telebot.TeleBot(API_KEY, parse_mode=None)
print("[SYSTEM] Start Bot")

@bot.callback_query_handler(func=lambda callback:True)
def callback_inline(callback):
  bot.delete_message(callback.message.chat.id, callback.message.message_id)
  
@bot.message_handler(commands=['createqr'])
def Createqr(msg):
	CreateQR(msg)
	
if (__name__ == "__main__"):
	
	Thread(targs=Createqr, args=(bot.infinity_polling())).start()
	
	Thread(targs=callback_inline, args=(bot.infinity_polling())).start()
