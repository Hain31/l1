import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('wage-data.csv')
print(df.head(5))

ser = df[df['State'] == 'California'].set_index('Year')['Salary']
#print(ser)
plt.plot(ser)
#plt.show()

'''Постройте линейный график изменения минимальной зарплаты (признак Salary), усредненной по всем штатам'''
dfg = df.groupby('Year')['Salary'].agg('mean')
#print(dfg)
plt.plot(dfg)
plt.title('Изменение минимальной зарплаты, усредненной по всем штатам')
plt.xlabel = 'Год'
plt.ylabel = 'Минимальная зарплата $\ч'

# метки на шкале X
x_range = list(range(dfg.index.min(), dfg.index.max(), 5))
x_range.append(dfg.index.max())
plt.xticks(x_range, rotation=45)
#plt.show()

#гистаграмы
s1 = df[df['Year'] == 2010]['Salary']
#print(s1)
w_b = s1.max() / 10
x_r = [i * w_b for i in range(11)]

plt.hist(s1, bins=10)
plt.title('Минимальная з.п. в 2010 году')
plt.xlabel = '$\ч'
plt.ylabel = 'количество записей'
plt.xticks(x_r)
#plt.show()

# точетные диаграммы
df_c = pd.read_csv('wage-data-coast.csv')

df0 = df_c[df_c['IsCoastal'] == 0]
plt.scatter(df0['Year'], df0['Salary'], label='Not Coastal')

df1 = df_c[df_c['IsCoastal'] == 1]
plt.scatter(df1['Year'], df1['Salary'], label='Coastal')

plt.title('Минимальная з.п. по годам')
plt.xlabel = 'Год'
plt.ylabel = '$\ч'

plt.legend()
#plt.show()

print(df_c[df_c['Year'] == 2017].sort_values('Salary', ascending=False).head(5))

# bar график
dfb = df_c[df_c['Year'] == 2015].groupby('IsCoastal')['Salary'].mean()
dfb = dfb.sort_values(ascending=True).reset_index()
dfb['IsCoastalStr'] = np.where(dfb['IsCoastal'] == 1, 'Coastal', 'Not Coastal')
print(dfb)

plt.bar(dfb['IsCoastalStr'], dfb['Salary'])
#plt.show()

# pie график
dfp = df_c[['IsCoastal', 'State']]
dfp['IsCoastalStr'] = np.where(df_c['IsCoastal'] == 1, 'Coastal', 'Not Coastal')
srp = dfp[['IsCoastalStr', 'State']].drop_duplicates().groupby('IsCoastalStr')['State'].count()
print(srp)

plt.pie(srp, labels=srp.index, autopct='%1.2f%%')
plt.show()




