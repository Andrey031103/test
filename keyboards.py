from telebot import types
from lexicon import lexicon

def get_main_menu_kb():

    button1 = types.InlineKeyboardButton(
        text=lexicon.to_fix_transaction.text,
        callback_data=lexicon.to_fix_transaction.data
    )

    button2 = types.InlineKeyboardButton(
        text=lexicon.to_budget_settings.text,
        callback_data=lexicon.to_budget_settings.data
    )

    button3 = types.InlineKeyboardButton(
        text=lexicon.to_reports.text,
        callback_data=lexicon.to_reports.data
    )

    main_menu_markup = types.InlineKeyboardMarkup()
    main_menu_markup.add(button1)
    main_menu_markup.add(button2)
    main_menu_markup.add(button3)
    return main_menu_markup

def get_transaction_type_kb():
    income_btn = types.InlineKeyboardButton(
        text=lexicon.select_income.text,
        callback_data=lexicon.select_income.data
    )
    
    expence_btn = types.InlineKeyboardButton(
        text=lexicon.select_expence.text,
        callback_data=lexicon.select_expence.data
    )

    get_back_btn =types.InlineKeyboardButton(
        text=lexicon.from_select_transaction_type.text,
        callback_data=lexicon.from_select_transaction_type.data
    )
    
    kb = types.InlineKeyboardMarkup()
    kb.add(income_btn)
    kb.add(expence_btn)
    kb.add(get_back_btn)
    
    return kb

def remove_old_kb():
    return types.ReplyKeyboardRemove()

def get_income_categories_kb():
    kb = types.InlineKeyboardMarkup()
        
    button1 = types.InlineKeyboardButton(
        text=lexicon.pocket_income.text,
        callback_data=lexicon.pocket_income.data
    )
    button2 = types.InlineKeyboardButton(
        text=lexicon.salary_income.text,
        callback_data=lexicon.salary_income.data
    )

    button3 = types.InlineKeyboardButton(
        text=lexicon.gift_income.text,
        callback_data=lexicon.gift_income.data
    )

    button4 = types.InlineKeyboardButton(
        text=lexicon.another_income.text,
        callback_data=lexicon.another_income.data
    )

    button5 = types.InlineKeyboardButton(
        text=lexicon.from_transaction_categorie.text,
        callback_data=lexicon.from_transaction_categorie.data
    )


    kb.add(button1)
    kb.add(button2)
    kb.add(button3)
    kb.add(button4)
    kb.add(button5)

    return kb


def get_expence_categoriers_kb():
    kb = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(
        text=lexicon.food_expence.text,
        callback_data=lexicon.food_expence.data
    )
    button2 = types.InlineKeyboardButton(
        text=lexicon.transport_expence.text,
        callback_data=lexicon.transport_expence.data

    )

    button3 = types.InlineKeyboardButton(
        text=lexicon.gift_expence.text,
        callback_data=lexicon.gift_expence.data
    )
    button4 = types.InlineKeyboardButton(
        text=lexicon.philanthropy_expence.text,
        callback_data=lexicon.philanthropy_expence.data
    )
    button5 = types.InlineKeyboardButton(
        text=lexicon.attractions_expence.text,
        callback_data=lexicon.attractions_expence.data
    )
    button6 = types.InlineKeyboardButton(
        text=lexicon.clothes_expence.text,
        callback_data=lexicon.clothes_expence.data
    )
    button7 = types.InlineKeyboardButton(
        text=lexicon.another_expence.text,
        callback_data=lexicon.another_expence.data
    )

    button8 = types.InlineKeyboardButton(
        text=lexicon.from_transaction_categorie.text,
        callback_data=lexicon.from_transaction_categorie.data
    )

    kb.add(button1)
    kb.add(button2)
    kb.add(button3)
    kb.add(button4)
    kb.add(button5)
    kb.add(button6)
    kb.add(button7)
    kb.add(button8)

    return kb

def get_back_to_category_kb():
    kb = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(
        text=lexicon.from_amount_to_category.text,
        callback_data=lexicon.from_amount_to_category.data
    )

    kb.add(btn)
    return kb
  