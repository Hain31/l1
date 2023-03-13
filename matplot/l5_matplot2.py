import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('wage-data-coast.csv')

fig, ax = plt.subplots(figsize=(12, 6))

data_w = df[df['State'] == 'Washington'][['Year', 'Salary']]
data_c = df[df['State'] == 'California'][['Year', 'Salary']]
#print(data)

ax.plot(data_w['Year'], data_w['Salary'], label='Washington')
ax.plot(data_c['Year'], data_c['Salary'], label='California')

ax.set_title('Минимальная зп', pad=20, color='red', backgroundcolor='pink')
ax.set_xlabel('Год')
ax.set_ylabel('ЗП $')
ax.set_xticks(list(range(data_w['Year'].min(), data_w['Year'].max(), 5)) + [data_w['Year'].max()])

ax.axvline(x=1999, color='red', linewidth=1, linestyle='--')

ax.legend()

plt.show()

#------------------------------
dat2000 = df[df['Year'] == 2000]['Salary']
dat2010 = df[df['Year'] == 2010]['Salary']

fig, ax = plt.subplots(figsize=(12, 6))

_, bins1, _ = ax.hist(dat2000, label='2000', alpha=0.5, bins=20)
ax.hist(dat2010, label='2010', alpha=0.5, bins=bins1)
ax.set_xticks(list(bins1))
ax.tick_params(axis='x', rotation=45)
ax.legend()

plt.show()

#----------------------------
for year in [2000, 2010]:
    dat = df[df['Year'] == year]['Salary']

    fig, ax = plt.subplots(figsize=(12, 6))

    _, bins1, _ = ax.hist(dat, bins=20)
    ax.set_xticks(list(bins1))
    ax.tick_params(axis='x', rotation=45)

plt.show()

#----------------------------
fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(12, 6))

_, bins1, _ = axs[1].hist(dat2010, bins=20)

axs[0].hist(dat2000, bins=bins1)

for ax in axs:
    ax.set_xticks(list(bins1))
    ax.tick_params(axis='x', rotation=45)

    for bin in bins1:
        ax.axvline(bin, color='lightgray', linewidth=1, linestyle='--')

plt.show()
