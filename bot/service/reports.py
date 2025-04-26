import matplotlib.pyplot as plt

def trend_line(data):
    aggregates = {}
    for d in data:
        formatted_date = d["date"].strftime("%m.%Y")
        type_ = d["type"]
        amount = d["amount"]
        if formatted_date not in aggregates:
            aggregates[formatted_date] = {'Доход': 0, 'Расход': 0}
    aggregates[formatted_date][type_] += amount

    print(aggregates)

    pre_data = []
    for d in aggregates:
        pre_data.append((d, aggregates[d]["Доход"], aggregates[d]['Расход']))

    months = []
    incomes = []
    expences = []
    for row in pre_data:
        months.append(row[0])
        incomes.append(row[1])
        expences.append(row[2])

    plt.plot(months, incomes, label='Доход')
    plt.plot(months, expences, label='Расход')
    plt.legend()
    plt.grid()
    plt.show()