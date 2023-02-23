
def fibonachu(num):
    cur_val = 0
    next_val = 1
    for _i in range(num):
        yield cur_val
        cur_val, next_val = next_val, cur_val+next_val

fib = fibonachu(10)

for fnum in fib:
    print(fnum, end=' ')

def square(nums):
    for num in nums:
        yield num ** 2

print('\n---')

print(sum(square(fibonachu(10))))

print('\n---')

cube_gen = (num ** 3 for num in fibonachu(10))

for i_num in cube_gen:
    print(i_num, end=' ')
