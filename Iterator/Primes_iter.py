# Итератор для вывода простых чисел

def is_num_primes(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True


class Primes:
    def __init__(self, limit):
        self.__limit = limit
        self.__cur_val = 2
        self.__next_val = 2

    def __iter__(self):
        self.__cur_val = 2
        self.__next_val = 2
        return self

    def __next__(self):

        self.__cur_val = self.__next_val

        while not is_num_primes(self.__next_val):
            self.__next_val += 1

        if self.__next_val > self.__limit:
            raise StopIteration

        self.__cur_val, self.__next_val = self.__next_val, self.__next_val + 1

        return self.__cur_val


m_Primes = Primes(50)
for i_num in m_Primes:
    print(i_num, end=' ')
