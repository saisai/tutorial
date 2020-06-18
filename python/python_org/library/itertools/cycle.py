
from itertools import cycle

#print(cycle(['a', 'b', 'c']))

ll = ['a', 'b', 'c']
s = 1

yy = cycle(ll)


for y in yy:
    if s <= 11:
        print(y)
    else:
        break
    s += 1

