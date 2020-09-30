
class Empty:
    pass

class LinkedStack:


    class _Node:

        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next


    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._head._element


    def pop(self):

        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

if __name__ == '__main__':
    ls = LinkedStack()
    ls.push(1)
    ls.push(2)
    ls.push(3)
    ls.push(4)
    ls.push(5)

    print(len(ls))
    while True:
        if ls.is_empty():
            break
        print(ls.pop())

