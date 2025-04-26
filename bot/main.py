from bot import bot
from handlers.user_handlers import register_user_handlers
from handlers.move_handlers import register_move_handlers

register_user_handlers(bot)
register_move_handlers(bot)


bot.polling(skip_pending=True) 
