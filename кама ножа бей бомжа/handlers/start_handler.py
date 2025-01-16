from lexicon import lexicon

def register_start_handler(bot):
    @bot.message_handler(commands=['start'])
    def start_handler(message):
        bot.send_message(chat_id=message.chat.id, text=lexicon.start)