from collections import deque

def tail(filename, n=10):
    'return the last n lines of a file'
    with open(filename) as f:
        return deque(f, n)


print(tail('vocabulary.txt'))
