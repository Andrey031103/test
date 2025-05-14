from lexicon import lexicon
from service.report import pie_chart
from service.database import read_database, trend_chart



def register_report_handlers(bot):

    @bot.callback_query_handler(
        func=lambda call: call.data == lexicon.to_reports.data
    )
    
    def send_report(callback):
        chat_id = callback.message.chat.id
        data = read_database(chat_id)
        bot.send_message(
            chat_id=chat_id,
            text='123456789'
        )
        pie = pie_chart(data)
        bot.send_photo(
            chat_id = chat_id,
            photo = pie
        )
        print(trend_chart(data))


