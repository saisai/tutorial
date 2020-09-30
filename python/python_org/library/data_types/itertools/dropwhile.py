from itertools import dropwhile


def func(x):
    print(x)
    x > 5

print(list(dropwhile(func, [1,2,3,4,5, 6])))


print(list(dropwhile(lambda x: x <= 14, range(10, 20))))


it = (i for i in range(10, 20))
a = dropwhile(lambda i_v: i_v[0] < 4, enumerate(it))
print(list(a))

def is_positive(n):
    return n > 0

value_list = [5, 6, -8, -4, 2]
result = list(dropwhile(is_positive, value_list))
print(result)

# https://stackoverflow.com/questions/12081864/difficulty-with-itertools-dropwhile
# https://www.geeksforgeeks.org/python-itertools-dropwhile/
