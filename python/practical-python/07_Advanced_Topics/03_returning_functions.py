
def add(x, y):
    def do_add():
        print('Adding', x, y)
        return x + y
    return do_add

a = add(3, 4)
print(a)
print(a())

print(add(1,2)())
