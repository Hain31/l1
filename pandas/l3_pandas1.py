import pandas as pd
import numpy as np
import math

df = pd.DataFrame([['Anna', 32, 3],
                   ['Serg', 40, 5],
                   ['Mike', 38, 4],
                   ['Smith', 80, None]])
df.columns = ['name', 'age', 'expr']

print(df)
print(type(df))
print(df['name'])
print(df.iloc[0])
print(df.iloc[:3, :2])
print(df[:3])

df.index = df['name']
print(df)
print(df.loc['Serg':'Smith', ['age', 'expr']])

print('\n---info---\n')
print(df.info())
print(df.shape)
print(df.describe())

print(df.dropna())
print(df[(df['age'] > 35) & (df['expr'] > 4)])

df['age2'] = df['age'] ** 2
print(df)

df['gender'] = [0, 1, 1, 1]
print(df)

df['no_work'] = df['age'] - df['expr']
print(df)

#------- ДЗ-----------
print('------- ДЗ-----------')

'''Загрузить массив NumPy из файла "arr_pandas.npy" (как в задании к предыдущему модулю) и преобразовать его в датафрейм. 
Массив содержит данные по результатам соревнований Scottish Hill Races в 2000 году (полное описание на английском языке 
можно посмотреть на странице с документацией по исходному файлу с данными).'''
arr = np.load('arr_pandas.npy', allow_pickle=True)
dat = pd.DataFrame(arr)
print(dat)

'''Определить, сколько в датафрейме строк и столбцов. Привести код и указать ответ в виде текста или комментария к коду.'''
print(dat.shape)

'''Присвоить столбцам следующие названия (указаны с пояснениями):

id: id участника
dist: расстояние в милях (по карте)
climb: высота, достигнутая на маршруте (в сумме за весь маршрут, в футах)
time: время (в часах)
timef: время для женщин (в часах)
type: тип гонки (hill, marathon, relay, uphill or other)'''

dat.columns = ['id', 'dist', 'climb', 'time', 'timef', 'type']
print(dat)

'''Вывести на экран значение высоты, достигнутой на маршруте участником Norman's Law.'''
print(int(dat[(dat['id'] == "Norman's Law")]['climb']))

'''Вывести на экран значения показателей dist, climb , time для первых 10 участников'''
print(dat.loc[:, ['dist', 'climb', 'time']].head(10))

'''Вывести на экран сводную информацию по датафрейму, которая включает типы всех столбцов. 
Сколько столбцов типа float в датафрейме? Привести ответ на вопрос в виде текста или комментария к коду.'''
print(dat.info())

'''Выбрать строки, которые соответствуют участникам эстафеты (relay).'''
print(dat[(dat['type'] == "relay")])

'''Выбрать строки, которые соответствуют участникам гонки в холмах (hill), которые в сумме достигли высоты более 1000 футов. Посчитать, сколько таких участников.'''
print(dat[(dat['type'] == "hill") & (dat['climb'] > 1000)])
print(dat[(dat['type'] == "hill") & (dat['climb'] > 1000)].shape[0])

'''Выбрать строки, соответствующие участникам, которые либо достигли высоты более 4000 футов, либо потратили менее 0.5 часов.'''
print(dat[((dat['time'] < 0.5) | (dat['time'] < 0.5))| (dat['climb'] > 4000)])

'''Создать столбец time_min, который содержит время маршрута, измеренное в минутах.'''
dat['time_min'] = dat['time'] * 60
print(dat.head())

'''Создать столбец year с годом соревнований (везде 2000 год). Внимание: столбец с годом должен быть числовым (целочисленным)'''
dat['year'] = 2000
print(dat.head())

#------- ДЗ доп-----------
print('------- ДЗ доп-----------')
'''Файл содержит результаты учебного психометрического исследования, целью которого является выявление связи между уровнем экстраверсии человека и его склонности к участию в волонтёрской деятельности. Датафрейм содержит следующие столбцы:

sex: пол респондента (Женский, Мужской);
volunteer: регулярное участие в волонтёрской деятельности (Да, Нет);
Q 1 - Q 57: ответы на вопросы по анкете Айзенка (Да, Нет), информацию об анкете и сами вопросы можно найти на этой странице.'''

ps = pd.read_csv("extraversion.csv", encoding="UTF-8")
print(ps.head())

'''Определить, сколько в датафрейме строк и столбцов. Привести код и указать ответ в виде текста или комментария к коду.'''
print(ps.shape)

'''Переименовать столбцы Q 1-Q 57 в Q1-Q57, другими словами, убрать в названиях всех столбцов пробелы в середине (если есть).'''
cols = ps.columns.tolist()
cols = [item.replace(' ', '') if item.startswith('Q') else item for item in cols ]
print(cols)
ps.columns = cols
print(ps.head())

'''Выбрать столбцы Q1, Q3, Q8, Q10, Q13, Q17, Q22, Q25, Q27, Q39, Q44, Q46, Q49, Q53, Q56 и сохранить их в отдельный датафрейм extra_yes.
Выбрать столбцы Q5, Q15, Q20, Q29, Q32, Q34, Q37,Q41, Q51 и сохранить их в отдельный датафрейм extra_no.
Эти столбцы будут использоваться для вычисления индекса экстраверсии.'''

extra_yes = ps.loc[:, ['Q1', 'Q3', 'Q8', 'Q10', 'Q13', 'Q17', 'Q22', 'Q25', 'Q27', 'Q39', 'Q44', 'Q46', 'Q49', 'Q53', 'Q56']]
print(extra_yes.head())
extra_no = ps.loc[:, ['Q5', 'Q15', 'Q20', 'Q29', 'Q32', 'Q34', 'Q37', 'Q41', 'Q51']]
print(extra_no.head())

'''Посчитать для каждой строки в датафрейме extra_yes число ответов "Да" и полученный результат сохранить в переменную extra_yes_sum. 
Посчитать для каждой строки в датафрейме extra_no число ответов "Нет" и полученный результат сохранить в переменную extra_no_sum.'''
extra_yes_sum = extra_yes.isin(['Да']).sum(axis=1)
print(extra_yes_sum)

extra_no_sum = extra_no.isin(['Нет']).sum(axis=1)
print(extra_no_sum)

'''Добавить в исходный датафрейм столбец extra, который представляет собой индекс экстраверсии, который считается так: 
сумма числа ответов "Да" в extra_yes и числа ответов "Нет" в extra_no.'''
ps['extra'] = extra_yes_sum + extra_no_sum
print(ps.head())

'''Добавить в исходный датафрейм столбец female, состоящий из значений 0 и 1 (0 — Мужской, 1 — Женский).
Подсказка: возможно, пригодится метод .astype() для Series в pandas, он преобразует типы столбцов.'''
ps['female'] = [1 if item == 'Женский' else 0 for item in ps['sex']]
print(ps.head())

'''Выбрать из исходного датафрейма строки, которые соответствуют либо волонтёрам с индексом экстраверсии выше 15, 
либо не-волонтёрам с индексом экстраверсии ниже 15. Сохранить в датафрейм pure.'''
pure = ps[((ps['volunteer'] == 'Да') & (ps['extra'] > 15)) | ((ps['volunteer'] == 'Нет') & (ps['extra'] < 15))]
print(pure.head())

'''Определить (любым способом, кроме явного подсчёта), сколько волонтёров и не-волонтёров в датафрейме pure.'''
print(pure[(pure['volunteer'] == 'Да')].shape[0])
print(pure[(pure['volunteer'] == 'Нет')].shape[0])

'''Определить минимальное, максимальное, среднее и медианное значение индекса экстраверсии в датафрейме pure. Сохранить полученные результаты в отдельные переменные (их должно быть 4).

Добавить в датафрейм pure столбец high, состоящий из 0 и 1, где 1 соответствует респондентам, уровень экстраверсии которых выше значения  𝑚=max{median,mean}, 
то есть максимума из медианного и среднего значения, а 0 — респондентам с уровнем экстраверсии не выше  𝑚.'''

min = pure['extra'].min()
max = pure['extra'].max()
mean = pure['extra'].mean()
median = pure['extra'].median()
print(f'min: {min}, max: {max}, mean: {mean}, median: {median},')

m = np.max([median, mean])

pure['high'] = [1 if item > m else 0 for item in pure['extra']]
print(pure)
