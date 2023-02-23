# бесконечный итератор
class СountIterator:

    def __int__(self):
        self.counter = 0

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        self.counter += 1
        return self.counter

m_counter = СountIterator()
for num in m_counter:
    print(num)
