import collections

print("From the right")
d = collections.deque('abcdefg')
while True:
    try:
        print(d.pop(), end='')
    except IndexError as e:
        print(e)
        break
print()

print('\n From the left')
d = collections.deque(range(6))
while True:
    try:
        print(d.popleft(), end='')
    except IndexError:
        break
print()
