
import collections

c = collections.Counter()
print('Initial: ', c)

c.update('abcdaab')
print('Sequenece :', c)

c.update({'a':1, 'd':5})
print('Dict :',c)
