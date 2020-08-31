
from collections import defaultdict
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]

d = defaultdict(set)
for k, v in s:
    d[k].add(v)

print(d)


s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1

sorted(d.items())
print(d)
