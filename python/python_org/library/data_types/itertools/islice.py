from itertools import islice


# slicing the range function

for i in islice(range(20), 5):
    print(i)


li = [2, 4, 5, 7, 8, 10, 20]

# Slicing the list
print(list(islice(li, 1, 6, 2)))


print(list(islice([1,2,3,4,5,6,7], 1, 4, 2)))


for ii in islice(range(50), 1, 30, 2):
    print(ii)

# https://www.geeksforgeeks.org/python-itertools-islice/

