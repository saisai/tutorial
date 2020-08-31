mystack = []

mystack.append('a')
mystack.append('b')
mystack.append('c')
print(mystack)

mystack.pop()
print(mystack)


mystack.pop()
print(mystack)

mystack.pop()
print(mystack)
#mystack.pop()
#print(mystack)


from collections import deque
mystack = deque()

mystack.append('a')
mystack.append('b')
mystack.append('c')

print(mystack)
mystack.pop()
print(mystack)
mystack.pop()
print(mystack)
mystack.pop()
print(mystack)
#mystack.pop()
#print(mystack)


from queue import LifoQueue

mystack = LifoQueue()
mystack.put('a')
mystack.put('b')
mystack.put('c')
print(mystack)
print(mystack.get())
print(mystack)
print(mystack.get())
print(mystack)


# https://realpython.com/how-to-implement-python-stack/

