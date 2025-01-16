from bot import bot
from handlers.start_handler import register_start_handler

register_start_handler(bot)

bot.polling()