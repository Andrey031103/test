import requests
import time
import sqlite3
import urllib3
import os

# Отключение предупреждений о безопасности
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Конфигурация
API_URL = "https://api.telegram.org/bot"
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Используйте переменную окружения для токена
PHOTO = "https://i.pinimg.com/736x/e0/6a/a8/e06aa88611f5e57da46025711f33902d.jpg"
MAX_COUNTRE = 100

# Создание и настройка базы данных
def setup_database():
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS updates (
        id INTEGER PRIMARY KEY,
        update_id INTEGER UNIQUE,
        chat_id INTEGER,
        message TEXT,
        photo_sent BOOLEAN
    )
    ''')
    conn.commit()
    return conn

# Функция для получения обновлений
def get_updates(offset):
    try:
        response = requests.get(f"{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}", verify=False)
        response.raise_for_status()  # Проверка на ошибки HTTP
        return response.json()
    except requests.RequestException as e:
        print(f"Ошибка при получении обновлений: {e}")
        return None

# Функция для отправки фотографии
def send_photo(chat_id):
    try:
        response = requests.get(f"{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={PHOTO}", verify=False)
        response.raise_for_status()  # Проверка на ошибки HTTP
        print(f"Фото отправлено в чат {chat_id}")
        return True
    except requests.RequestException as e:
        print(f"Ошибка при отправке фото в чат {chat_id}: {e}")
        return False

# Функция для сохранения обновлений в базу данных
def save_update(conn, update_id, chat_id, message, photo_sent):
    cursor = conn.cursor()
    cursor.execute('''
    INSERT OR IGNORE INTO updates (update_id, chat_id, message, photo_sent)
    VALUES (?, ?, ?, ?)
    ''', (update_id, chat_id, message, photo_sent))
    conn.commit()

# Основная программа
def main():
    conn = setup_database()
    offset = -2
    counter = 0

    while counter < MAX_COUNTRE:
        updates = get_updates(offset)
        if updates and "result" in updates:
            for result in updates["result"]:
                offset = result['update_id']
                if "message" in result:
                    chat_id = result["message"]["chat"]["id"]
                    message = result["message"].get("text", "")

                    # Отправка фото и сохранение информации в базу данных
                    photo_sent = send_photo(chat_id)
                    save_update(conn, offset, chat_id, message, photo_sent)

        time.sleep(2)  # Задержка между запросами
        counter += 1

    conn.close()

# Исправлено условие для запуска основной функции
if __name__ == "__main__":
    main()
