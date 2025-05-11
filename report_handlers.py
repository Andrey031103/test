from lexicon import lexicon

def register_report_handlers(bot):

    @bot.callback_query_handler(
        func=lambda call: call.data == lexicon.to_reports.data
    )
    
    def send_report(callback):
        chat_id = callback.message.chat.id
        bot.send_message(
            chat_id=chat_id,
            text='12345678910'
        )