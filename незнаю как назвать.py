import telebot
from telebot import types

TOKEN = '7596537784:AAF7P1oXCmuJQ7pORDlGaT4YfHPeTcawQHo'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True
    )
    keyboard.add(
        types.KeyboardButton(text=' efhl vy'),
        types.KeyboardButton(text='rbo bruobyv'),
    
    )   
    
    bot.send_message(chat_id=message.chat.id, text='Выберите вариант', reply_markup=keyboard)

bot.polling()
