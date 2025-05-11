from bot import bot
from lexicon import lexicon
from keyboards import get_main_menu_kb

def register_user_handlers(bot):
    @bot.message_handler(commands=["start"])
    def start_handler(message):
        bot.send_message(
            chat_id=message.chat.id,
            text=lexicon.start,
            reply_markup=get_main_menu_kb()
        )