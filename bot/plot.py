import matplotlib.pyplot as plt
from service.datadase import read_database

data = read_database(6170800646)

# data1 = [35,25,20,20]
# label1 = ['A','B','C','D']

# data2 = [50,35,15]
# label2 = ['E','F','G']

# fig, (ax1,ax2) = plt.subplots(1,2, figsize=(10,5))

# ax1.pie(data1, labels=label1, autopct='%1.1f%%')
# ax1.set_title('Диграмма доходов')
# ax2.pie(data2, labels=label2, autopct='%1.1f%%')
# ax2.set_title('Диаграмма дожодов')

# fig.suptitle('Доходы и расходы в категориях')
# plt.show()

from service.getter_categories import attrs_lexicon

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

print(expences_tmp_titles, incomes_tmp_titles)

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
ax1.set_title('Диаграмма доходов')
ax2.pie(expences_values, labels=expences_titles, autopct='%1.1f%%')
ax2.set_title('Диаграмма доходов')

fig.suptitle('Доходы и расходы в категориях')
plt.show()
