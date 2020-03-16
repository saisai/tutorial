

class Deque:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):

        try:
            item = self.items[self.n]

        except IndexError:
            raise StopIteration
        self.n += 1
        return item


if __name__ == '__main__':
    d = Deque()
    print(d.isEmpty())
    d.addRear(4)
    d.addRear('dog')
    print(list(d))
    d.addFront('cat')
    d.addFront(True)
    print(list(d))
    print(d.size())
    print(d.isEmpty())
    d.addRear(8.4)
    print(list(d))
    print(d.removeRear())
    print(d.removeFront())
    print(list(d))
