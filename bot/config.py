from environs import Env
import os
import csv

env = Env()
env.read_env()
bot_token = env("BOT_TOKEN")
database_path = "database.csv"

if not os.path.exists(database_path):
    with open("database.csv", "a", encoding="utf-8") as file:
        fieldnames = ["date","type","category","amount","chat_id"] 
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        