


def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('done')


for i in countdown(5):
    print(i)
