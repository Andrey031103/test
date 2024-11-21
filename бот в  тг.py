import requests
import time
from  pprint import pprint

API_URL = "https://api.telegram.org/bot"
BOT_TOKEN = "7596537784:AAF7P1oXCmuJQ7pORDlGaT4YfHPeTcawQHo"
TEXT  = "https://steamuserimages-a.akamaihd.net/ugc/961965309962870407/5E8015A9C722F4615034D9421D13EB7A160001EB/?imw=512&amp;imh=576&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=true"
MAX_COUNTRE = 100
offset = -2
counter = 0

while counter < MAX_COUNTRE:
    updates = requests.get(f"{API_URL}{BOT_TOKEN}/getUpdates?offset={offset+1}").json()
    pprint(updates)
    if updates["result"]:
        for result in updates["result"]:
            offset = result['update_id']
            chat_id = result["message"]["chat"]["id"]
            requests.get(f"{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={TEXT}")

    time.sleep(2)
    counter += 1
