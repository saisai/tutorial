from collections import defaultdict

s = [f.strip('\n') for f in open('vocabulary.txt', 'r')]


d = defaultdict(int)

for k in s:
    for w in k:
        d[w] += 1

print(d)
