import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')

df = pd.read_csv('vgsales.csv')
print(df.info())

'''Постройте линейный график динамики объёма продаж всех игр жанра «Sports» в Японии. Задайте графику размер 12 на 6.'''
dat_S = df[df['Genre'] == 'Sports'].groupby('Year')['JP_Sales'].sum()

#fig, ax = plt.subplots(figsize=(12, 6))
#sns.lineplot(data=dat_S, ax=ax)
#plt.show()

'''В одних координатных осях постройте линейные графики динамики продаж студии «Activision» в Северной Америке, Европе, Японии и во всем мире.'''
dat_All = df[df['Publisher'] == 'Activision'].groupby('Year')[['JP_Sales', 'NA_Sales', 'EU_Sales', 'Global_Sales']].sum()

#fig, ax = plt.subplots(figsize=(12, 6))
#sns.lineplot(data=dat_All, ax=ax)
#plt.show()

'''В цикле (т.е. на разных координатных осях) постройте линейные графики динамики продаж студии «Activision» в 
Северной Америке, Европе, Японии и во всем мире.'''

regS = ['JP_Sales', 'NA_Sales', 'EU_Sales', 'Global_Sales']

'''fig, ax = plt.subplots(nrows=4, ncols=1, figsize=(8, 8))

for i, reg in enumerate(regS):
    sns.lineplot(data=dat_All[reg], ax=ax[i])

plt.show()'''

'''Постройте PairPlot для всех численных признаков датасета. Разным цветом укажите цвета для разных платформ.
Примечание: при построении этого графика pandas может выдавать предупреждения (warnings), в этой задаче такое поведение допустимо.'''

#sns.pairplot(df, hue='Platform') #, corner=True
#plt.show()

'''В одной координатной сетке постройте 2 гистограммы распредения мировых продаж игр издателей «Microsoft Game Studios» и «Take-Two Interactive» 
после 2010 года (включая 2010 год). Графики сделайте полупрозрачными, отсечки должны быть общими и соответствовать ширине столбцов обоих графиков.'''
dat_MSTT = df[((df['Publisher'] == 'Microsoft Game Studios') | (df['Publisher'] == 'Take-Two Interactive')) & (df['Year'] >= 2010)]

#sns.histplot(data=dat_MSTT, x='Global_Sales', hue='Publisher', alpha=0.5, bins=30)
#plt.show()

'''Постройте линейный график динамики количества игр, выпускаемых Nintendo, по годам. 
С помощью numpy или pandas определите промежуток, в который издатель каждый год выпускал больше 35 игр, и подсветите этот 
промежуток времени с помощью зелёного полупрозрачного прямоугольника.'''
dat_Nint35 = df[df['Publisher'] == 'Nintendo'].groupby('Year')['Name'].count()
dat_Le35 = dat_Nint35[dat_Nint35 > 35]

#fig, ax = plt.subplots(figsize=(12, 6))
#sns.lineplot(data=dat_Nint35)
#ax.axvspan(xmin=dat_Le35.index[0], xmax=dat_Le35.index[-1], color='green', alpha=0.5)
#plt.show()

'''Определите 3 жанра и 4 платформы с самыми большими продажами игр в мире за всё время. 
Постройте сетку графиков 4 на 3, в каждой ячейке постройте точечный график, проверяющий зависимость общемировых продаж от 
продаж в Северной Америке для каждой пары (жанра, платформы). Разными цветами укажите игры разных годов. 
Размер итогового полотна определите самостоятельно таким образом, чтобы все графики были видны.
Делайте графики достаточно читаемыми, чтобы из них можно было сделать вывод о наличии / отсутствии зависимостей в данных.'''
dat_G3 = df.groupby('Genre')[['Global_Sales']].sum().sort_values('Global_Sales', ascending=False).head(3)
dat_P4 = df.groupby('Publisher')[['Global_Sales']].sum().sort_values('Global_Sales', ascending=False).head(4)
print(list(dat_G3.index))
print(list(dat_P4.index))

dat_rrr = df[(df['Genre'].isin(list(dat_G3.index))) & (df['Publisher'].isin(list(dat_P4.index)))]

g = sns.FacetGrid(data=dat_rrr, row='Genre', col='Publisher', hue='Year')
g.map(sns.scatterplot, 'Global_Sales', 'NA_Sales' )

plt.show()