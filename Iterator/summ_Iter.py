# сумма 2х случайных чисел
import random

class RandomSumm:

    def __init__(self, limit):
        self.__limit = limit
        self.__count = 0
        self.__num = 0

    def __iter__(self):
        self.__count = 0
        self.__num = 0
        return self

    def __next__(self):
        if self.__limit > self.__count:
            self.__count += 1
            new_num = self.__num + random.random()
            self.__num = new_num
            return new_num
        else:
            raise StopIteration


m_random = RandomSumm(10)
for num in m_random:
    print(num)

print('---')

for num in m_random:
    print(num)
