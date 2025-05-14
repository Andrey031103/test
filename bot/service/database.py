from datetime import datetime
from config import database_path
import csv

def write_database(data):
    with open(database_path, "a", encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerow(data.values())

def beautify(row):
    row["date"] = datetime.strptime(row["date"], "%d.%m.%Y")
    row['amount'] = int(row['amount'])
    row['chat_id'] = int(row['chat_id'])
def read_database(chat_id):
     with open(database_path, "r", encoding="utf8") as file:
        reader = csv.DictReader(file)
        my_data = []
        for row in reader:
             if row ['chat_id'] == str(chat_id):
                beautify(row)
                my_data.append(row)

        return my_data
