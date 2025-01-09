import telebot
from telebot import types

TOKEN = '7596537784:AAF7P1oXCmuJQ7pORDlGaT4YfHPeTcawQHo'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(1,30):
        btn = types.KeyboardButton(text='Кнопка' + str(i))
        kb.add(btn)
    
    bot.send_message(chat_id=message.chat.id, text='Выберите вариант', reply_markup=kb)

@bot.message_handler(func=lambda x: x.text == "Кнопка 1")
def process_button_1(message):
    bot.send_message(chat_id = message.chat.id, text='Кнопка 52')

@bot.message_handler(func=lambda x: x.text == "Кнопка 2")
def process_button_1(message):
    bot.send_message(chat_id = message.chat.id, text='Кнопка 53')

@bot.message_handler(commands=['hide'])
def process_button_1(message):
    bot.send_message(chat_id=message.chat.id, text='Клавиатура ушла домой', reply_markup=types.ReplyKeyboardRemove())


bot.polling()
