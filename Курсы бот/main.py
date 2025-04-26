import logging
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ConversationHandler
)

# Замените на ваши данные
API_TOKEN = '7687285080:AAGp8QTRUwET-YFzTJFnRuLOvuxH9ylyjSI'
EXCHANGE_API_URL = 'https://v6.exchangerate-api.com/v6/5a6daa99153defa15bf6502a/latest/USD'
CRYPTO_API_URL = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,ripple&vs_currencies=usd'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Константы для ConversationHandler
WAITING_FOR_CURRENCY = 1

# Хранение истории запросов
history = []

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💱 Курсы валют", callback_data='currency')],
        [InlineKeyboardButton("💰 Курсы криптовалют", callback_data='crypto')],
        [InlineKeyboardButton("📜 История запросов", callback_data='history')],
        [InlineKeyboardButton("ℹ️ Помощь", callback_data='help')],
        [InlineKeyboardButton("🔍 Поиск валюты/криптовалюты", callback_data='search')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Привет! Я бот для получения курсов валют и криптовалют. Используйте кнопки ниже:",
        reply_markup=reply_markup
    )

async def get_currency_rates(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(EXCHANGE_API_URL)
        data = response.json()
        
        if data['result'] == 'success':
            rates = data['conversion_rates']
            message = (
                "📊 Курсы валют к USD:\n"
                f"🇪🇺 EUR: {rates['EUR']:.2f}\n"
                f"🇷🇺 RUB: {rates['RUB']:.2f}\n"
                f"🇬🇧 GBP: {rates['GBP']:.2f}\n"
                f"🇯🇵 JPY: {rates['JPY']:.2f}\n"
                f"🇨🇳 CNY: {rates['CNY']:.2f}"
            )
            history.append("Запрос курсов валют")
        else:
            message = "❌ Ошибка получения данных"
    except Exception as e:
        logging.error(f"Currency error: {e}")
        message = "❌ Ошибка соединения"

    query = update.callback_query
    await query.edit_message_text(message, reply_markup=get_back_keyboard())


async def get_crypto_rates(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(CRYPTO_API_URL)
        data = response.json()
        
        message = "📈 Курсы криптовалют:\n"
        for crypto in ['bitcoin', 'ethereum', 'ripple']:
            price = data[crypto]['usd']
            message += f"• {crypto.capitalize()}: ${price:.2f}\n"
            history.append(f"Запрос {crypto}")
    except Exception as e:
        logging.error(f"Crypto error: {e}")
        message = "❌ Ошибка получения данных"

    query = update.callback_query
    await query.edit_message_text(message.strip(), reply_markup=get_back_keyboard())


async def show_history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if not history:
        await query.edit_message_text("История запросов пуста", reply_markup=get_back_keyboard())
        return

    last_requests = history[-10:]  # Показываем последние 10 запросов
    message = "📅 История запросов:\n" + "\n".join(
        f"{i+1}. {req}" for i, req in enumerate(last_requests)
    )
    await query.edit_message_text(message, reply_markup=get_back_keyboard())


async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "ℹ️ Помощь по использованию бота:\n\n"
        "• Используйте кнопки для навигации\n"
        "• Курсы валют обновляются в реальном времени\n"
        "• История сохраняет последние 10 запросов\n"
        "• В поиске можно вводить: BTC, ETH, EUR, RUB и др.\n\n"
        "Команды:\n"
        "/start - Главное меню\n"
        "/help - Эта справка"
    )
    
    query = update.callback_query
    await query.edit_message_text(help_text, reply_markup=get_back_keyboard())

async def search_currency(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "Введите название валюты (например: EUR, RUB) или криптовалюты (например: bitcoin):",
        reply_markup=get_back_keyboard()
    )
    return WAITING_FOR_CURRENCY  # Возвращаем состояние для ConversationHandler

async def handle_currency_search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.upper()
    response_message = ""
    
    try:
        # Проверяем сначала криптовалюты
        crypto_response = requests.get(CRYPTO_API_URL)
        crypto_data = crypto_response.json()
        
        if user_input.lower() in crypto_data:
            rate = crypto_data[user_input.lower()]['usd']
            response_message = f"🏦 {user_input}: ${rate:.2f}"
            history.append(f"Поиск: {user_input} - ${rate:.2f}")
        else:
            # Проверяем валюты
            currency_response = requests.get(EXCHANGE_API_URL)
            currency_data = currency_response.json()
            
            if currency_data['result'] == 'success':
                rate = currency_data['conversion_rates'].get(user_input)
                if rate:
                    response_message = f"💵 {user_input}: {rate:.2f} USD"
                    history.append(f"Поиск: {user_input} - {rate:.2f} USD")
                else:
                    response_message = "🚫 Валюта не найдена"
    except Exception as e:
        logging.error(f"Ошибка поиска: {e}")
        response_message = "❌ Ошибка при поиске"

    await update.message.reply_text(response_message, reply_markup=get_back_keyboard())
    return ConversationHandler.END  # Завершаем диалог

def get_back_keyboard():
    keyboard = [[InlineKeyboardButton("🔙 Назад", callback_data='back')]]
    return InlineKeyboardMarkup(keyboard)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'currency':
        await get_currency_rates(update, context)
    elif query.data == 'crypto':
        await get_crypto_rates(update, context)
    elif query.data == 'history':
        await show_history(update, context)
    elif query.data == 'help':
        await cmd_help(update, context)
    elif query.data == 'search':
        await search_currency(update, context)
    elif query.data == 'back':
        await return_to_main_menu(query)

async def return_to_main_menu(query):
    keyboard = [
        [InlineKeyboardButton("💱 Курсы валют", callback_data='currency')],
        [InlineKeyboardButton("💰 Курсы криптовалют", callback_data='crypto')],
        [InlineKeyboardButton("📜 История запросов", callback_data='history')],
        [InlineKeyboardButton("ℹ️ Помощь", callback_data='help')],
        [InlineKeyboardButton("🔍 Поиск валюты/криптовалюты", callback_data='search')]
    ]
    await query.edit_message_text(
        "Главное меню:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def main():
    application = ApplicationBuilder().token(API_TOKEN).build()

    # Добавляем ConversationHandler для обработки поиска
    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(search_currency, pattern='^search$')],
        states={
            WAITING_FOR_CURRENCY: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_currency_search)]
        },
        fallbacks=[]
    )

    application.add_handler(CommandHandler("start", cmd_start))
    application.add_handler(conv_handler)
    application.add_handler(CallbackQueryHandler(button_handler))

    application.run_polling()

if __name__ == '__main__':
    main()