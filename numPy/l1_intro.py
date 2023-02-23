import numpy as np

arr = np.array([[1, 2, 3, 4],
                [3, 2, 1, 6],
                [5, 7, 3, 9]])

print('Количество измерений', arr.ndim)
print('Размер', arr.size)
print('Размерность', arr.shape)

print('arr[1][1]', arr[1][1])
print('arr[1][1]', arr[1, 1])

print('Срезы\n', arr[:, ::2], '\n------\n', arr[1:3, ::2])

arr2 = np.array([5, 6, 2, 7, 8, 23, 4])

print('min, argmin', arr2.min(), arr2.argmin())
print('mean, mean, median', arr2.mean(), np.mean(arr2), np.median(arr2))

grades = np.array([[3, 5, 4, 3, 4],
                   [4, 3, 4, 3, 5],
                   [2, 3, 3, 2, 3]])

print('\n axis=0 \n', grades.mean(axis=0), '\n axis=1 \n', grades.mean(axis=1))

newarr = np.arange(2, 15, 2.5)
print('\n new array', newarr)

newarrZ = np.zeros((3, 4, 2))
print('\n new array Z\n', newarrZ)

newarrE = np.eye(5)
print('\n new array E\n', newarrE)

ages = np.array([[15, 32, 23, 45, 60],
                 [45, 24, 70, 12, 40],
                 [77, 16, 11, 54, 90]])

agesB = (ages >= 18) & (ages <= 60)

print('\nбулев массив\n', agesB, '\nвсего работников\n', np.sum(agesB))

print('\nВозраст работников\n', ages[(ages >= 18) & (ages <= 60)])

# ДЗ
print('\n---ДЗ---\n')
scores = np.array([[20, 40, 56, 80, 0, 5, 25, 27, 74, 1],
 [0, 98, 67, 100, 8, 56, 34, 82, 100, 7],
 [78, 54, 23, 79, 100, 0, 0, 42, 95, 83],
 [51, 50, 47, 23, 100, 94, 25, 48, 38, 77],
 [90, 87, 41, 89, 52, 0, 5, 17, 28, 99],
 [32, 18, 21, 18, 29, 31, 48, 62, 76, 22],
 [6, 0, 65, 78, 43, 22, 38, 88, 94, 100],
 [77, 28, 39, 41, 0, 81, 45, 54, 98, 12],
 [66, 0, 88, 0, 44, 0, 55, 100, 12, 11],
 [17, 70, 86, 96, 56, 23, 32, 49, 70, 80],
 [20, 24, 76, 50, 29, 40, 3, 2, 5, 11],
 [33, 63, 28, 40, 51, 100, 98, 87, 22, 30],
 [16, 54, 78, 12, 25, 35, 10, 19, 67, 0],
 [100, 88, 24, 33, 47, 56, 62, 34, 77, 53],
 [50, 89, 70, 72, 56, 29, 15, 20, 0, 0]])

ex1 = np.sum(scores == 0)

print('Получили 0 балов:', ex1)

ex3 = np.sum((scores >= 50) & (scores <= 70))

print('\nПолучили 50-70 балов:', ex3)

ex4 = scores.mean(axis=1)
print('\nСредний бал по группам:', ex4)

ex4 = ex4.argmax()
print('\nВысший средний бал в группе:', ex4 + 1)

ex5 = scores[(scores > 0)]
print('\nОценки выше 0:\n', ex5)

ex6 = ex5.min()
print('\nМинимальный бал по всем группам:', ex6)

ex7 = ex5[ex5 > 80]
print('\nПродвинутые балы:', ex7)

print('\nРазмерность:', ex7.ndim)

print('\nФорма:', ex7.shape)

print('\nРазмер:', ex7.size)

ex11 = scores == 100

print('\nТолько 100 балов:', ex11)

print('\nОценки первых 7 групп\n', scores[:7,:])