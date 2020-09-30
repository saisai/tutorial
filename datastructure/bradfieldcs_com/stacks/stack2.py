class Stack:

    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == None

    def push(self, item):
        self._items.insert(0, item)

    def pop(self):
        return self._items.pop(0)

    def peek(self):
        return self._items[0]

    def size(self):
        return len(self._items)

    def __next__(self):
        count = 0
        while count < self.size():
            yield self._items[0]
            count += 1
if __name__ == '__main__':
    s = Stack()
    print(s.is_empty())
    s.push("hello")
    s.push("world")
    s.push(1)
    s.push(True)
    print(s.peek())
    print(s.size())
    print(list(s))
