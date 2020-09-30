
import inspect
from pprint import pprint

class MyObj:

    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        print(" testing __eq__ ({}, {})".format(self.val, other.val))
        return self.val == other.val

print("Methods\n")
pprint(inspect.getmembers(MyObj, inspect.isfunction))

