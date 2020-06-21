#from functions import cmp_to_key


def cmp_to_key(mycmp):
    "Convert a cmp= function into a key= function"
    class K(object):
        def __init__(self, obj, *args):
            print("obj created with ", obj)
            self.obj = obj

        def __lt__(self, other):
            print("comparing less than ", self.obj)
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            print("comparing greater than ", self.obj)
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            print("comparing equal to ", self.obj)
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            print("comapring less than eqal ", self.obj)
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            print("comparing greater than eqal ",self.obj)
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            print("comapring not equal ", self.obj)
            return mycmp(self.obj, other.obj) != 0

    return K

def mycmp(a, b):
    print("In mycmp for ", a, ' ', b)
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0


print(sorted([3,4,2,5], key=cmp_to_key(mycmp)))


# https://stackoverflow.com/questions/32752739/python-how-does-the-functools-cmp-to-key-function-works
