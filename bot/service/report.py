import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from service.getter_categories import attrs_lexicon
from io import BytesIO

def trend_chart(data):
    aggregates = {}
    for d in data:
        formatted_date = d["data"].strftime("%d.%m.%Y")
        type_ = d["type"]
        amount = d["amount"]
        if formatted_date not in aggregates:
            aggregates[formatted_date] = {"Доход":0,"Расход":0,}
        aggregates[formatted_date][type_] += amount


    pre_data = []
    for d in aggregates:
        pre_data.append((d, aggregates[d]["Доход"], aggregates[d]["Расход"]))
    

    months = []
    incomes = []
    expences = []
    for d in pre_data:
        months.append(d[0])
        incomes.append(d[1])
        expences.append(d[2])
    print(months)
    




def pie_chart(data):
    plt.cla()
    plt.clf()
    plt.close("all")

    expences = []
    incomes = []
    for obj in attrs_lexicon:
        if obj[0].endswith('expence'):
            expences.append(obj)
        elif obj[0].endswith('income'):
            incomes.append(obj)

    expences_tmp_titles =[]
    incomes_tmp_titles = []
    for e in expences:
        expences_tmp_titles.append(e[1].text)
    for i in incomes:
        incomes_tmp_titles.append(i[1].text)

    

    to_pie = {"income": {"sum":0},"expence": {"sum":0}}
    for d in data:
        category = d['category']
        amount = d['amount']
        

        if d['type'] == 'Доход':
            type_ = 'income'
        elif d['type'] == 'Расход':
            type_ ='expence'

        if category not in to_pie[type_]:
            to_pie[type_][category] = 0
        to_pie[type_][category] += amount
        to_pie[type_]["sum"] += amount

    expences_titles = []
    expences_values = []

    incomes_titles = []
    incomes_values = []

    for e in expences_tmp_titles:
        if e in to_pie["expence"]:
            value = to_pie["expence"][e] / to_pie["expence"]["sum"] * 100
            expences_titles.append(e)
            expences_values.append(value)

    for i in incomes_tmp_titles:
        if i in to_pie["income"]:
            value = to_pie["income"][i] / to_pie["income"]["sum"] * 100
            incomes_titles.append(i)
            incomes_values.append(value)

    fig, (ax1,ax2) = plt.subplots(1,2, figsize=(10,5))

    ax1.pie(incomes_values, labels=incomes_titles, autopct='%1.1f%%')
    ax1.set_title('Диаграмма расходов')
    ax2.pie(expences_values, labels=expences_titles, autopct='%1.1f%%')
    ax2.set_title('Диаграмма доходов')

    fig.suptitle('Доходы и расходы в категориях')
    buf = BytesIO()
    fig.savefig(buf, format="png")
    print(fig)
    buf.seek(0)

    return buf