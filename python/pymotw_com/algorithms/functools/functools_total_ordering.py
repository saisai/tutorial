import functools
import inspect
from pprint import pprint


@functools.total_ordering
class MyObject:

    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        print(' testing __eq__({}, {})'.format(
            self.val, other.val
        ))
        return self.val == other.val

    def __gt__(self, other):
        print('  testing __gt__({}, {})'.format(
            self.val, other.val
        ))
        return self.val > other.val

print('MEthods \n')
pprint(inspect.getmembers(MyObject, inspect.isfunction))
pprint(inspect.getmembers(MyObject, inspect.istraceback))
pprint(inspect.getmembers(MyObject, inspect.isbuiltin))

a = MyObject(1)
b = MyObject(2)

print('\n Comparisons:')
for expr in ['a < b', 'a <= b', 'a == b', 'a >= b', 'a > b']:
    print('\n{:<6}:'.format(expr))
    result = eval(expr)
    print(' result of {}: {}'.format(expr, result))
