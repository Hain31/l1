import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')

df = pd.read_csv('wage-data-coast.csv')
print(df.info())

dat1 = df[df['State'].isin(['Alaska', 'California', 'Arizona', 'Florida'])]

fig, ax = plt.subplots(figsize=(12, 6))

sns.lineplot(data=dat1, x='Year', y='Salary', hue='State', ax=ax)

ax.set_title('График 4 штатов')
ax.set_xlabel('год')
ax.set_ylabel('ЗП')

plt.show()

#----------------
dat2 = df[df['Year'] == 2000]

ax = sns.histplot(data=dat2, x='Salary', hue='IsCoastal', bins=25)

ax.set_title('Гистаграмма минимальных ЗП')
ax.set_xlabel('ЗП')
ax.set_ylabel('Количество')

plt.show()

#---------------
df2 = pd.read_csv('wage-data-coast-with-population.csv')
print(df2.info())

'''Постройте точечный график, на котором по оси х будет указан год, а на оси у - население. 
Задайте цвет каждой отметки в зависимости от величины минимальной зарплаты в конкретном штате и конкретном году.'''

fig, ax = plt.subplots(figsize=(12, 8))
sns.scatterplot(data=df2, x='Year', y='Population', hue='Salary', style='IsCoastal', ax=ax)

plt.show()

#----------------
df3 = sns.load_dataset('diamonds')

print(df3.info())

#sns.pairplot(df3, hue='cut') #, corner=True
#plt.show()

#g = sns.FacetGrid(df3, row='cut', col='color', hue='clarity')
#g.map(sns.scatterplot, 'carat', 'price')
#g.add_legend()
#plt.show()

#g = sns.FacetGrid(df3, row='cut', col='color', hue='clarity')
#g.map(sns.histplot, 'price')
#g.add_legend()
#plt.show()

'''Постройте FacetGrid, в котором строкам сетки будут соответствовать значения чистоты бриллианта, а столбцам сетки - значения огранки.
Внутри сетки постройте точечные графики зависимости цены от высоты бриллианта (это параметр z). 
Разным цветом на графиках укажите бриллианты разного цвета.'''

g = sns.FacetGrid(df3, row='clarity', col='cut', hue='color', palette='rocket')
g.map(sns.scatterplot, 'z', 'price')
g.add_legend()
plt.show()