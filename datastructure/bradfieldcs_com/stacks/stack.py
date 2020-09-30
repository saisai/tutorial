class Stack:

    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def size(self):
        return len(self._items)

    def __iter__(self):
        count = 0
        while count < len(self._items):
            yield self._items[count]
            count += 1


if __name__ == '__main__':

    s = Stack()
    print(s.is_empty())
    s.push('hello')
    s.push(True)
    s.push(1)
    s.push(20.0)
    s.push(lambda x: x)
    s.push(id)
    s.push(iter)
    print(s.peek())
    print(s.size())
    print(list(s))
