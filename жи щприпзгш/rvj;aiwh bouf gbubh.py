import telebot
from telebot import types

TOKEN = '7596537784:AAF7P1oXCmuJQ7pORDlGaT4YfHPeTcawQHo'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Кнопка 1', callback_data='btn1')
    btn2 = types.InlineKeyboardButton(text='Кнопка 2', callback_data='btn2')
    btn3 = types.InlineKeyboardButton(text='Кнопка 3', callback_data='btn3')

    markup.row(btn1,btn2)
    markup.add(btn3)

    bot.send_message(chat_id=message.chat.id, text='Привет, бот не работает', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'btn1')
def handle_btn1(collback):
    bot.send_message(chat_id=collback.message.chat.id, text='Кнопка 1 нажата')

@bot.callback_query_handler(func=lambda callback: callback.data == 'btn2')
def handle_btn1(collback):
    bot.send_message(chat_id=collback.message.chat.id, text='кнопка 2 ушла')

@bot.callback_query_handler(func=lambda callback: callback.data == 'btn3')
def handle_btn1(collback):
    bot.send_message(chat_id=collback.message.chat.id, text='Кнопка 3 не дома')
    
   
    
bot.polling()
