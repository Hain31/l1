import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''Описание данных
Этот датасет содержит информацию о суммарных продажах видеоигр для игровых консолей. Описание признаков:
    Rank - порядковый номер записи в датасете
    Name - наименование игры
    Platform - платформа, для которой выпущена игра (Nintendo, PlayStation, XBox и др.)
    Year - год выпуска игры
    Genre - жанр игры
    Publisher - наименование компании-издателя игры
    NA_Sales - объем продаж игры в Северной Америке, млн. копий
    EU_Sales - объем продаж игры в Европе, млн. копий
    JP_Sales - объем продаж игры в Японии, млн. копий
    Other_Sales - объем продаж игры в остальных странах, млн. копий
    Global_Sales - объем продаж игры по всему миру, млн. копий'''

df = pd.read_csv('vgsales.csv')

'''Постройте линейный график динамики объема продаж всех игр жанра "Sports" в Японии. Задайте графику размер 12 на 6'''
dat1 = df[df['Genre'] == "Sports"][['Year', 'JP_Sales']].groupby('Year')['JP_Sales'].sum()

print(dat1)

#fig, ax = plt.subplots(figsize=(12, 6))
#ax.plot(dat1)
#plt.show()

'''В одних координатных осях постройте линейные графики динамики продаж студии "Activision" в Северной Америке, Европе, Японии и всем мире'''
dat2 = df[df['Publisher'] == "Activision"][['Year', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Global_Sales']].groupby('Year').agg('sum')
print(dat2)

#fig, ax = plt.subplots(figsize=(12, 6))
#ax.plot(dat2['NA_Sales'], label='NA_Sales')
#ax.plot(dat2['JP_Sales'], label='JP_Sales')
#ax.plot(dat2['Global_Sales'], label='Global_Sales')
#ax.legend()
#plt.show()

'''В цикле (т.е. на разных координатных осях) постройте линейные графики динамики продаж студии "Activision" в 
Северной Америке, Европе, Японии и всем мире'''

rList = [ 'NA_Sales', 'JP_Sales', 'Global_Sales']

#fig, axs = plt.subplots(nrows=3, ncols=1,figsize=(12, 8))

#for i, reg in enumerate(rList):
#    axs[i].plot(dat2[reg])
#    axs[i].set_title(reg)

#plt.show()

'''Постройте такие же линейные графики динамики продаж студии "Activision" в Северной Америке, Европе, Японии и всем мире на одном полотне в сетке 2 на 2 графика. 
Итоговое полотно сделайте размером 12 на 12. Все графики должны разделять оси X и Y'''

rList = [['NA_Sales', 'EU_Sales'],
         ['JP_Sales', 'Global_Sales']]

#fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 12))

#for i, reg0 in enumerate(rList):
#    for j, reg in enumerate(reg0):
#        axs[i, j].plot(dat2[reg])
#        axs[i, j].set_title(reg)

#plt.show()

'''В одной координатной сетке постройте 2 гистограммы распределения мировых продаж игр издателей 
"Microsoft Game Studios" и "Take-Two Interactive" после 2010 года (включая 2010 год). 
Графики сделайте полупрозрачными, отсечки должны быть общими и соответствовать ширине столбцов обоих графиков'''

datH_MS = df[(df['Year'] >= 2010) & (df['Publisher'] == "Microsoft Game Studios")]['Global_Sales']
datH_TT = df[(df['Year'] >= 2010) & (df['Publisher'] == "Take-Two Interactive")]['Global_Sales']

#fig, ax = plt.subplots(figsize=(12, 8))

#_, bins1, _ = ax.hist(datH_MS, alpha=0.5, bins=20, label="Microsoft Game Studios")
#ax.hist(datH_TT, alpha=0.5, bins=bins1, label="Take-Two Interactive")

#ax.set_xticks(list(bins1))
#ax.legend()

#plt.show()

'''Определите 5 платформ, для которых в Японии было продано больше всего игр за все время. 
Проиллюстрируйте величину продаж на столбчатой диаграмме, столбец с самым высоким значением окрасьте зеленым, а с самым низким - красным'''

dat_J5 = df.groupby('Platform')['JP_Sales'].sum().sort_values(ascending=False).head()
print(dat_J5.info())

#fig, ax = plt.subplots(figsize=(12, 6))
#bk = ax.bar(dat_J5.index, dat_J5)
#bk[0].set_color('g')
#bk[4].set_color('r')

#plt.show()

'''Постройте линейный график динамики количества игр, выпускаемых Nintendo, по годам. С помощью numpy или pandas определите промежуток, 
в который издатель каждый год выпускал больше 35 игр, и подсветите этот промежуток времени с помощью зеленого полупрозрачного прямоугольника'''

dat_Nint35 = df[df['Publisher'] == 'Nintendo'].groupby('Year')['Name'].count()
dat_Le35 = dat_Nint35[dat_Nint35 > 35]
print(dat_Nint35)
print(dat_Le35)

#fig, ax = plt.subplots(figsize=(12, 6))

#ax.plot(dat_Nint35)
#ax.axvspan(xmin=dat_Le35.index[0], xmax=dat_Le35.index[-1], color='green', alpha=0.5)

#plt.show()

'''Определите 3 жанра и 4 издателя с самыми большими продажами игр в мире за все время. Постройте сетку графиков 4 на 3, 
в каждой ячейке постройте точечный график, проверяющий зависимость общемировых продаж от продаж в Северной Америке для каждой пары (жанр, издатель). 
Размер итогового полотна определите самостоятельно таким образом, чтобы все графики были видны'''

dat_G3 = df.groupby('Genre')[['Global_Sales']].sum().sort_values('Global_Sales', ascending=False).head(3)
dat_P4 = df.groupby('Publisher')[['Global_Sales']].sum().sort_values('Global_Sales', ascending=False).head(4)

print(dat_G3, dat_P4)

fig, axs = plt.subplots(nrows=3, ncols=4, figsize=(17, 14))

for i, genre in enumerate(dat_G3.index):
    for j, publ in enumerate(dat_P4.index):
        dfGY2 = df[(df['Genre'] == genre) & (df['Publisher'] == publ)].groupby('Year')[['Global_Sales', 'NA_Sales']].agg('sum')

        #axs[i, j].scatter(dfGY2.index, dfGY2['Global_Sales'], label='Global Sales')
        #axs[i, j].scatter(dfGY2.index, dfGY2['NA_Sales'], label='NA Sales')
        axs[i, j].plot(dfGY2.index, dfGY2['Global_Sales'], label='Global Sales')
        axs[i, j].plot(dfGY2.index, dfGY2['NA_Sales'], label='NA Sales')
        axs[i, j].set_title(publ + ' - ' + genre)
        axs[i, j].set_xlabel = 'Год'
        axs[i, j].set_ylabel = 'Продажи'
        axs[i, j].legend()

#fig.set_title('Зависимость продаж во всем мире от продаж в Северной Америке')

plt.show()
