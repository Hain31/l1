import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''----------ДЗ---------'''
print('----------ДЗ---------')
'''Для выполнения домашнего задания необходимо использовать датасет vgsales.csv, загрузка которого будет приведена ниже. 
Этот датасет содержит информацию о суммарных продажах видеоигр для игровых консолей. Описание признаков:

Rank – порядковый номер записи в датасете
Name – наименование игры
Platform – платформа, для которой выпущена игра (Nintendo, PlayStation, XBox и др.)
Year – год выпуска игры
Genre – жанр игры
Publisher – наименование компании-издателя игры
NA_Sales – объем продаж игры в Северной Америке, млн. копий
EU_Sales – объем продаж игры в Европе, млн. копий
JP_Sales – объем продаж игры в Японии, млн. копий
Other_Sales – объем продаж игры в остальных странах, млн. копий
Global_Sales – объем продаж игры по всему миру, млн. копий'''

df = pd.read_csv('vgsales.csv')
print(df.head())

'''Постройте гистограмму распределения объема продаж всех игр в Японии.'''
sJ = df['JP_Sales']
#plt.hist(sJ, bins=10)
#plt.show()

'''Постройте столбчатую диаграмму (barchart), показывающую сравнение общемирового объема продаж игры "Grand Theft Auto V" на разных платформах.'''
dfGTA = df[df['Name'] == "Grand Theft Auto V"]
dfGTA = dfGTA[['Platform','Global_Sales']].sort_values('Global_Sales', ascending=False)
print(dfGTA)
#plt.bar(dfGTA['Platform'], dfGTA['Global_Sales'])
#plt.title('Cравнение общемирового объема продаж игры "Grand Theft Auto V" на разных платформах')
#plt.show()

'''Постройте линейный график динамики суммарных общемировых продаж всех игр по годам.'''
dfGY = df.groupby('Year')['Global_Sales'].agg('sum')
print(dfGY)
#plt.plot(dfGY)
#plt.title('динамика суммарных общемировых продаж всех игр по годам')
#plt.xlabel = 'Год'
#plt.ylabel = 'Продажи'
#plt.show()

'''Постройте точечную диаграмму, показывающую существование зависимости продаж во всем мире от продаж в Северной Америке.'''
dfGY2 = df.groupby('Year')['Global_Sales', 'NA_Sales'].agg('sum')
print(dfGY2)

#plt.scatter(dfGY2.index, dfGY2['Global_Sales'], label='Global Sales')
#plt.scatter(dfGY2.index, dfGY2['NA_Sales'], label='NA Sales')
#plt.title('зависимость продаж во всем мире от продаж в Северной Америке')
#plt.xlabel = 'Год'
#plt.ylabel = 'Продажи'
#plt.legend()
#plt.show()

'''Постройте круговую диаграмму процентного соотношения продаж игры "Super Mario Bros." на разных платформах во всем мире. 
Подпишите доли графика с точностью 1 знак после запятой.'''
dfSM = df[df['Name'] == "Super Mario Bros."][['Platform', 'Global_Sales']].groupby('Platform')['Global_Sales'].agg('sum')
print(dfSM)
#plt.pie(dfSM, labels=dfSM.index, autopct='%1.1f%%')
#plt.show()

'''Определите 5 издателей, имеющих наибольшие суммарные продажи во всём мире в 2013 году, и проиллюстрируйте величину их продаж на столбчатой диаграмме.'''
df5H = df[df['Year'] == 2013][['Name', 'Global_Sales']].groupby('Name').sum().sort_values('Global_Sales', ascending=False).head(5)
print(df5H)
#plt.bar(df5H.index, df5H['Global_Sales'])
#plt.show()

'''Постройте гистограмму распределения величины общемировых продаж игр, выпущенных не издателем Nintendo, в период с 2000 по 2015 год включительно. 
Гистограмма для большей точности должна содержать 20 столбцов, отсечки на оси X должны соответствовать границам столбцов.'''
dfAll = df[(df['Publisher'] != 'Nintendo') & (df['Year'] >= 2000) & (df['Year'] <= 2015)]['Global_Sales']
print(dfAll)

w_b = dfAll.max() / 20
x_r = [i * w_b for i in range(21)]
x_r.append(dfAll.max())

#plt.hist(dfAll, bins=20)
#plt.xticks(x_r)
#plt.show()

'''Постройте линейный график динамики суммарных мировых продаж игр жанра "Action" по годам.'''
dfArc = df[df['Genre'] == "Action"][['Year', 'Global_Sales']].groupby('Year').agg('sum')
print(dfArc)

#plt.plot(dfArc)
#plt.show()

'''С помощью столбчатой диаграммы проиллюстрируйте объем продаж всех игр издателя "Microsoft Game Studios" в 
Северной Америке за все время в зависимости от жанра. Столбцы расположите по убыванию.'''
dfMSNA = df[(df['Publisher'] == "Microsoft Game Studios")][['Genre', 'NA_Sales']].groupby('Genre').agg('sum').sort_values('NA_Sales', ascending=False)
print(dfMSNA)

#plt.bar(dfMSNA.index, dfMSNA['NA_Sales'])
#plt.xticks(rotation=45)
#plt.show()

'''Одной из основных задач при анализе данных является проверка данных на корректность и отсутствие ошибок. 
В датасете "vgsales" одним из потенциальных источников ошибок является столбец с общемировыми продажами.
По идее, значение общемировых продаж какой-либо игры должно равняться сумме продаж в Северной Америке, Европе, Японии и остальных странах,
 в противном случае мы получим ошибку в данных, которая может негативно повлиять на весь дальнейший процесс анализа.

Причин возникновения такой ошибки может быть несколько. Давайте рассмотрим следующие причины:

Ошибка округления. В целом, такая ошибка достаточно часто встречается при переводе величин из одних единиц в другие 
(например, из тысяч копий в миллионы копий).
Ошибка вычислений. Такая ситуация требует более серьезного исследования, поскольку она может привести к недостоверным результатам анализа данных.
Будем считать, что в записи имеется ошибка суммирования, если сумма продаж какой-либо игры в Северной Америке, Европе, Японии и остальных странах
отличается от общемировых продаж более, чем на 0.01 млн копий.

С помощью круговой диаграммы проиллюстрируйте процент записей в датасете, имеющих такую ошибку суммирования продаж.'''

df['isError'] = np.where(np.abs(df['Global_Sales'] - (df['NA_Sales'] + df['EU_Sales'] + df['JP_Sales'] + df['Other_Sales'])) > 0.01, 'Error', 'Not error')
print(df[['Global_Sales','NA_Sales','EU_Sales','JP_Sales','Other_Sales', 'isError']].head(10))

dfE = df[['isError', 'Global_Sales']].groupby('isError')['Global_Sales'].agg('count')
print(dfE)

plt.pie(dfE, labels=dfE.index,  autopct='%1.2f%%')
plt.show()