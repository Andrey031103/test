import telebot
import sqlite3
import os

TOKEN = '7596537784:AAF7P1oXCmuJQ7pORDlGaT4YfHPeTcawQHo'  # Замените на ваш токен
bot = telebot.TeleBot(TOKEN)

# Функция для инициализации базы данных
def init_db():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            file_path TEXT NOT NULL
        )
    ''')

    # Добавляем книги в таблицу
    books = [
        {"title": "Дубровский", "file_path": "books/Дубровский"},
        {"title": "Война и мир", "file_path": "books/Tolstoy_Voina_i_mir.pdf"}
    ]

    for book in books:
        cursor.execute('INSERT OR IGNORE INTO books (title, file_path) VALUES (?, ?)',
                       (book["title"], book["file_path"]))

    conn.commit()
    conn.close()

# Создаем папку для книг, если она не существует
if not os.path.exists('Библиотека'):
    os.makedirs('Библиотека')

# Инициализируем базу данных
init_db()

@bot.message_handler(commands=['support'])
def process_command_start(message):
  text = ('Подержка пока не доступна.\n\n'
          'Вы пока можете написать лично мне\n'
          '@An234d\n')
  bot.send_message(chat_id=message.chat.id, text=text)


@bot.message_handler(commands=['start'])
def process_command_start(message):
    text = ('Привет! Я бот для загрузки и поиска книг StellarBook.\n\n'
            'Чтобы загрузить книгу, отправьте файл с названием книги.\n'
            'Чтобы найти книгу, просто напишите её название.\n'
            'Чтобы обратиться в подержку напишите /support\n'
            'Чтобы прочитать про StellarBook, просто напишите /description \n\n')
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['description'])
def process_command_start(message):
  text = ('StellarBook: '
          'это электронная библиотка книг в телеграмм.'
          'В этой библиотеке вы можете отправлять книги pdf файлом и искать их.')
  bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(content_types=['document'])
def handle_document(message):
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # Сохраняем файл на сервере
        file_name = message.document.file_name
        file_path = os.path.join('books', file_name)

        # Сохраняем файл в папке books
        with open(file_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        # Сохраняем информацию о книге в базе данных
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO books (title, file_path) VALUES (?, ?)', (file_name, file_path))
        conn.commit()
        conn.close()

        bot.send_message(chat_id=message.chat.id, text=f'Книга "{file_name}" успешно загружена!')
    except Exception as e:
        bot.send_message(chat_id=message.chat.id, text='Произошла ошибка при загрузке книги. Пожалуйста, попробуйте еще раз.')
        print(f'Error: {e}')

@bot.message_handler(func=lambda message: True)
def search_book(message):
    title = message.text
    try:
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute('SELECT file_path FROM books WHERE title LIKE ?', ('%' + title + '%',))
        results = cursor.fetchall()
        conn.close()

        if results:
            for result in results:
                file_path = result[0]
                with open(file_path, 'rb') as file:
                    bot.send_document(chat_id=message.chat.id, document=file)
        else:
            bot.send_message(chat_id=message.chat.id, text='Книга не найдена. Попробуйте другое название.')
    except Exception as e:
        bot.send_message(chat_id=message.chat.id, text='Произошла ошибка при поиске книги. Пожалуйста, попробуйте еще раз.')
        print(f'Error: {e}')

bot.infinity_polling()
