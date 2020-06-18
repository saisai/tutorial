from itertools import groupby
import json

L = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]

# key function
key_func = lambda x: x[0]

for key, group in groupby(L, key_func):
    print(key + " :", list(group))


a_list = [("Animal", "cat"),
          ("Animal", "dog"),
          ("Bird", "peacock"),
          ("Bird", "pigeon")]

a_dict = {}
an_iterator = groupby(a_list, lambda x: x[0])

for key, group in an_iterator:
    #key_and_group = {key: list(group)}
    a_dict.update({key:list(group)})
    #print(key_and_group)

print(a_dict)
print(json.dumps(a_dict))

r = [k for k, g in groupby('AAAABBBCCDAABBB')]
print(r)

g = [list(g) for k, g in groupby('AAAABBBCCD')]
print(g)
# https://www.geeksforgeeks.org/itertools-groupby-in-python
# https://stackoverflow.com/questions/773/how-do-i-use-itertools-groupby
