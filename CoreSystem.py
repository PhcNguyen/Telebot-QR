from time import sleep
from KEY import API_KEY
from telebot import types
from random import randint
import os
import telebot
import qrcode

bot = telebot.TeleBot(API_KEY, parse_mode=None)

def SendMsg(msg, text):
	markup = types.InlineKeyboardMarkup()
	box = types.InlineKeyboardButton(text="Delete", callback_data="1")
	markup.row(box)
	bot.send_message(msg.chat.id, f"{text}", reply_markup=markup)
	
def Delete(msg):
	chat_id = msg.chat.id
	message_id = msg.message_id
	bot.delete_message(chat_id=chat_id, message_id=message_id)

def CmdChat(msg):
	user = msg.from_user.id
	text = msg.text
	print(f"\nUser: {user}\nChat: {text}")

def CreateQR(msg):
	
	def SettingCreate(data, RandomCode):
		qr = qrcode.QRCode(
		version=1,
		error_correction=qrcode.constants.ERROR_CORRECT_L,
		box_size=10,
		border=4,
		)
		qr.add_data(data)
		qr.make(fit=True)
		img = qr.make_image(fill_color="white", back_color="black")
		img.save(f"qrcode{RandomCode}.png")
	
	def SendImage(msg, RadomCode):
		image_path = f"qrcode{RandomCode}.png"
		with open(image_path, 'rb') as photo:
			bot.send_photo(msg.chat.id, photo)
			
	def DeleteFile(RandomCode):
		path = f"qrcode{RandomCode}.png"
		try:
			os.remove(path)
			print(f'The file {path} has been deleted successfully.')
		except FileNotFoundError:
			print(f'The file {path} does not exist.')
	Cmdchat(msg)
	A = 100000 ; B = 999999
	RandomCode = randint(A, B)
	text = msg.text
	print(text)
	text = text.split()
	del text[0]
	if len(text) == 0:
		SendMsg(msg, "Error")
		return 0
	else:
		SettingCreate(text, RandomCode)
		SendImage(msg, RandomCode)
		DeleteFile(RandomCode)
		Delete(msg)
