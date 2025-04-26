class CallbackLexicon:
    def __init__(self, text, data):
        self.text = text
        self.data = data

class Lexicon:    
    def __init__(self):
        self.start = "Это бот для учета финансов. Ты можешь вести журнал доходов и расходов," \
                     "Но и контролировать свой бюджет."
                     
        self.to_fix_transaction = CallbackLexicon(
            text="Зафиксировать транзакцию",
            data="to_fix_transaction"
        )
        
        self.to_budget_settings = CallbackLexicon(
            text="Настройка бюджета",
            data="to_budget_settings"
        )
        
        self.to_reports = CallbackLexicon(
            text="Отчеты",
            data="to_reports"
        )
        
        self.select_income = CallbackLexicon(
            text="Доход",
            data="income_transaction"
        )
        
        self.select_expence = CallbackLexicon(
            text="Расход",
            data="expence_transaction"
        )

        self.pocket_income = CallbackLexicon(
            text='Карманные',
            data='salary_income'
        )

        self.salary_income = CallbackLexicon(
            text='Зарплата',
            data='salary_income'
        )

        self.gift_income = CallbackLexicon(
            text='Подарок',
            data='gift_income'

        )

        self.another_income = CallbackLexicon(
            text='Другое',
            data='another_income'
        )

        self.philanthropy_expence = CallbackLexicon(
            text='Благотворительность',
            data='philanthropy_expence'
        )

        self.food_expence = CallbackLexicon(
            text='Питание',
            data='food_income'
        )

        self.transport_expence = CallbackLexicon(
            text='Транспорт',
            data='transport_income'
        )

        self.attractions_expence = CallbackLexicon(
            text='Развлечения',
            data='attractions_income'
        )

        self.clothes_expence = CallbackLexicon(
            text='Одежда',
            data='clothes_income'
        )

        self.gift_expence = CallbackLexicon(
            text='Подарок',
            data='gift_expence'
        )

        self.another_expence = CallbackLexicon(
            text='Другое',
            data='another_expence'
        )

        self.from_transaction_categorie = CallbackLexicon(
            text='Выход из ада',
            data='from_transaction_categorie'
        )


        self.from_select_transaction_type = CallbackLexicon(
            text='Выход из ада',
            data='from_select_transaction_type'
        )

        self.from_amount_to_category = CallbackLexicon(
            text='Выход из ада',
            data='from_amount_to_category'
        )

        self.fixed_transaction = "Дата: {date}\nТип: {type}\nКатегория: {category}\nСумма: {amount}"

    
lexicon = Lexicon()