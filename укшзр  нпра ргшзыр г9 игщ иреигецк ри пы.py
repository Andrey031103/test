import telebot
import random

TOKEN = '7596537784:AAF7P1oXCmuJQ7pORDlGaT4YfHPeTcawQHo'
bot = telebot.TeleBot(TOKEN)
users={

}


ATTEMPTS = 5

def get_random_number():
    return random.randint(1, 100)

@bot.message_handler(commands=['cancel'])
def process_canel_command(message):
    chat_id = message.chat.id
    user = users[message.chat.id]
    if user['in_game']:
        user['in_game'] = False
        text = 'Вы вышли из игры!'
    else:
        text = 'Может сыграем разок!'
    bot.send_message(chat_id=chat_id, text=text)
@bot.message_handler(commands=['start'])
def process_command_start(message):
    user = {
    'in_game': False,
    'secret_number': None,
    'attempts': None,
    'total_games': 0,
    'wins': 0
    } 
    users[message.chat.id] = user
    if message.chat.id not in users:
        users[message.chat.id] = user
    text = ('Привет, давай сыграем в игру "Угадай число"?\n\n'
            'Чтобы получить правила игры введите /help\n\n'
            'Давай сыграем?')
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['help'])
def process__help_command(message):
    text = f'Правила игры; \n\nЯ загадываю число от 1 до 100,'\
           f'а вам нужно его угадать\nУ вас есть {ATTEMPTS}'\
           f'попыток\n\nДоступные команды:\n/help - правила'\
           f'игры и список команд\n/cancel - выйти из игры\n'\
           f'/start - посмотреть статистику\n\nДавай сыграем?'
    bot.send_message(chat_id=message.chat.id,text=text)

def check_play(message):
    return message.text.lower() in ['да', 'давай', 'ок']

@bot.message_handler(func=check_play)
def process_positive_answer(message):
    chat_id = message.chat.id
    user = users[chat_id]
    if not user['in_game']:
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user["attempts"] = ATTEMPTS
        text = 'Ура, я загадал число от 1 до 100, попробуй отгадать'
        user["total_games"] += 1
        bot.send_message(chat_id=message.chat.id, text=text)

def is_valid_number(message):
    return message.text and message.text.isdigit() and int(message.text) >= 1 and int(message.text) <= 100

@bot.message_handler(func=is_valid_number)
def process_number_answer(message):
    chat_id = message.chat.id
    user = users[message.chat.id]
    if user['in_game'] == True:
        if int(message.text) == user["secret_number"]:
            text = "УРА!!! Ты отгадал число! Ты молодец. Давай сыграем еще?"
            bot.send_message(chat_id=chat_id, text=text)
            user['in_game'] = False
            user["wins"] += 1
        elif int(message.text) > user["secret_number"]:
            user["attempts"] -= 1
            bot.send_message(chat_id=chat_id, text="Мое число меньше")
        elif int(message.text) < user["secret_number"]:
            user["attempts"] -= 1
            bot.send_message(chat_id=chat_id, text="Мое число больше")
        if user["attempts"] == 0:
            user["in_game"] = False
            text = f"Попыток не осталось, вы проиграли. Мое число было {user['secret_number']}. Сыграем еще?"
            bot.send_message(chat_id=chat_id, text=text)
    else:
        bot.send_message(chat_id=chat_id, text="Мы еще не играем. Хотите сыграть?")
       
@bot.message_handler(commands=["stat"]) 
def process_stat_command(message):
    winrate = 0
    user = users[message.chat.id]
    if user['total_games'] != 0:
        winrate = user['wins'] / user['total_games'] * 100
    text =  f"Всего игр сыграно: {user['total_games']}\n" \
            f"Игр выиграно: {user['wins']}\n" \
            f"% побед: {winrate}"
    bot.send_message(chat_id=message.chat.id, text=text)
    
bot.infinity_polling()
