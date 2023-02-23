import os

# бесконечный генератор
def infinity_num():
    __i = 0
    while True:
        yield __i
        __i += 1


for i_num in infinity_num():
    print(i_num, end=' ')


# генератор для чтения файла

fl = open('data.txt', 'r')
data = fl.read()
print(data)