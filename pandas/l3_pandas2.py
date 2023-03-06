import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('WeightLoss.csv')
print(df.head(5))

df['avo'] = df.loc[:, 'w1':'w3'].apply(np.mean, axis=1)
print(df.head(5))

f = lambda x: x.max() - x.min()
df['wwh'] = df.loc[:, 'w1':'w3'].apply(f, axis=1)
print(df.head(5))

def f1(items=[]):
    result = items.median()
    return result

df['wmed'] = df.loc[:, 'w1':'w3'].apply(f1, axis=1)
print(df.head(5))

#группировка
print(df.groupby('group').agg(['mean', 'median']))

print(df.groupby('group').min())

#сортировка
print(df.sort_values(['se3', 'avo'], ascending=True).head(10)) #inplace=True

# работа с Nan
print(df.info())

print(df.fillna(0))
df = df.dropna()
print(df.info())

# ----------- ДЗ -------------
print('----------- ДЗ -------------')

'''Описание переменных в датафрейме:

mode: выбранный тип рыбалки: на берегу (beach), на пирсе (pier), в своей лодке (boat) и в арендованной лодке (charter);
price: стоимость выбранного типа рыбалки;
catch: коэффициент улова при выбранном типе рыбалки;
pbeach: стоимость рыбалки на берегу;
ppier: стоимость рыбалки на пирсе;
pboat: стоимость рыбалки на своей лодке;
pcharter: стоимость рыбалки на арендованной лодке;
cbeach: коэффициент улова на рыбалке на берегу;
cpier: коэффициент улова на рыбалке на пирсе;
cboat: коэффициент улова на рыбалке на своей лодке;
ccharter: коэффициент улова на рыбалке на арендованной лодке;
income: доход в месяц.'''

'''Загрузить таблицу из файла Fishing.csv и сохранить её в датафрейм dat. Вывести на экран первые 8 строк загруженного датафрейма.'''
dat = pd.read_csv('Fishing.csv')
print(dat.head(5))

'''Добавить, используя метод .apply(), столбец log_income, содержащий натуральный логарифм доходов респондентов.'''
dat['log_income'] = dat['income'].apply('log')
print(dat.head(5))

'''Посчитать для каждого респондента абсолютное значение отклонения price от pbeach и сохранить результат в столбец pdiff.'''
f = lambda x : abs(x[0] - x[1])
dat['pdiff'] = dat.loc[:, ['price', 'pbeach']].apply(f, axis=1)
print(dat.loc[:, ['price', 'pbeach', 'pdiff']].head(5))

'''Сгруппировать наблюдения в таблице по признаку тип рыбалки (mode) и вывести для каждого типа среднюю цену (price), 
которую респонденты заплатили за рыбалку.'''
print(dat.groupby('mode').agg('mean')['price'])

'''Сгруппировать наблюдения в таблице по признаку тип рыбалки (mode) и вывести для каждого типа разницу между медианным и 
средним значением цены (price), которую респонденты заплатили за рыбалку.'''
datPr = dat.groupby('mode').agg(['median', 'mean'])['price']
print(datPr['median'] - datPr['mean'])

f1 = lambda x: np.median(x) - np.mean(x)
print(dat.groupby('mode').agg(f1)['price'])

'''Сгруппировать наблюдения в таблице по признаку тип рыбалки (mode) и сохранить полученные датафреймы (один для каждого типа рыбалки) в 
отдельные csv-файлы. В итоге должно получиться четыре разных csv-файла.'''
#for name, data in dat.groupby("mode"):
    #data.to_csv("Fish_" + name + ".csv")

'''Отсортировать строки в датафрейме в соответствии со значениями income в порядке убывания таким образом, 
чтобы результаты сортировки сохранились в исходном датафрейме.'''
dat.sort_values('income', ascending=False, inplace=True)
print(dat.head(10))

'''Отсортировать строки в датафрейме в соответствии со значениями price и income в порядке возрастания. 
Можно ли сказать, что люди с более низким доходом и выбравшие более дешёвый тип рыбалки, в целом, предпочитают один тип рыбалки, 
а люди с более высоким доходом и более дорогой рыбалкой – другой? Ответ записать в виде текстовой ячейки или в виде комментария.'''
dat.sort_values(['price', 'income'], ascending=True, inplace=True)
print(dat.head(20)[['price', 'income', 'mode']])

'''Любым известным способом проверить, есть ли в датафрейме пропущенные значения. Если есть, удалить строки с пропущенными значениями.
 Если нет, написать комментарий, что таких нет.'''
print(dat.info())

dat.dropna(inplace=True)
print(dat.info())

'''Загрузить датафрейм из файла wgi_fh.csv, учитывая, что в качестве разделителя столбцов используется точка с запятой, 
а в качестве десятичного разделителя – запятая (опции sep= и decimal= в функции read_csv() соответственно).

Файл содержит данные за 2016 по различным политологическим индексам. Датафрейм содержит следующие столбцы:

country: страна;
cnt_code: код страны (аббревиатура);
year: год;
va: индекс подотчётности Voice & Accountability (WGI);
ps: индекс политической стабильности Political Stability and Lack of Violence (WGI);
ge: индекс эффективности правительства Government Effectiveness (WGI);
rq: индекс качества управления Regulatory Quality (WGI);
rl: индекс верховенства закона Rule of Law (WGI);
cc: индекс контроля коррупции Control of Corruption (WGI);
fh: индекс свободы Freedom House (Freedom Rating).'''
dat2 = pd.read_csv('wgi_fh.csv', sep=';', decimal=',')
print(dat2.head(10))

'''Вывести общую информацию по датафрейму: число строк и столбцов, типы данных в таблице. 
Есть ли в таблице пропущенные значения? Привести код и дать ответ в виде комментария.'''
print(dat2.info())

'''Если в датафрейме есть строки с пропущенными значениями, удалить их. Сохранить изменения в исходном датафрейме.'''
dat2.dropna(inplace=True)
print(dat2.info())

'''Назвать строки в датафрейме в соответствии со столбцом cnt_code. Удалить данный столбец из датафрейма.'''
dat2.set_index(dat2['cnt_code'], inplace=True)
dat2.drop('cnt_code', axis=1, inplace=True)
print(dat2.head(10))

'''Отсортировать строки в таблице в соответствии со значениями столбцов с индексами Control of Corruption и Voice & Accountability 
таким образом, чтобы результаты сортировки были сохранены сразу в исходном датафрейме.'''
dat2.sort_values(['cc', 'va'], inplace=True)
print(dat2.head(10))

'''Используя метод .apply(), создать столбец cc_round со значениями индекса Control of Corruption, округлёнными до первого знака после запятой.'''
f_round = lambda x: np.round(x, 1)
dat2['cc_round'] = dat2['cc'].apply(f_round)
print(dat2.head(5))

'''Добавить в датафрейм столбец fh_status, в котором будут храниться типы стран в зависимости от значения индекса Freedom House 
(значения типов стран: "free", "partly free", "not free"). Соответствие значений fh типам стран см. в Table 3 в конце этой страницы.

Подсказка: здесь понадобится функция, которая возвращает разные значения в зависимости от выполнения условий. 
Её можно написать через def или lambda. Больше про функции можно почитать на pythontutor.ru.'''
def f_staus(x):
    if (x >=1) and (x <= 2.5):
        return 'free'
    elif (x >= 3) and (x <= 5):
        return 'partly free'
    else:
        return "not free"

dat2['fh_status'] = dat2['fh'].apply(f_staus)
print(dat2.head(5))

'''Сгруппировать строки в датафрейме в соответствии со значениями столбца fh_status, полученного в предыдущем задании и вывести минимальное, 
среднее и максимальное значение показателя Political Stability and Lack of Violence по каждой группе.'''

print(dat2.groupby('fh_status')['ps'].agg(['min', 'mean', 'max']))

'''Создайте (любым способом) маленький датафрейм, состоящий из двух столбцов:
fh_type: тип страны;
count: число стран данного типа.
Постройте, используя полученный датафрейм, столбиковую диаграмму (barplot), опираясь на эту документацию. 
Чтобы увидеть график явно, прямо в текущем ноутбуке, допишите в начале ячейки с кодом для графика следующую строку:'''
gd = dat2.groupby('fh_status')['fh_status'].agg('count')
print('----')
print(gd['free'])

ax = gd.plot.bar()
plt.show()
