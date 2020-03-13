class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __iter__(self):
        self.n = 0      
        return self

    def __next__(self):
        #print(self.n)
        try:
            item = self.items[self.n]           
        except IndexError:
            raise StopIteration
        self.n += 1
        return item

if __name__ == '__main__':
    q = Queue()

    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())
    print(list(q))


