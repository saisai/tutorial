class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None


class UnorderedList(object):

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        print(temp)
        self.head = temp


    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next

        return count

    def search(self, item):
        current = self.head

        while current is not None:
            if current.value == item:
                return True
            current = current.next
        return False

    def remove(self, item):
        current =self.head
        previous = None

        while True:
            if current.value == item:
                break
            previous, current = current, current.next

        if previous is None:
            self.head = current.next
        else:
            previous.next= current.next
            
    def __iter__(self):
        return self 
        
    def __next__(self):   
        if self.size():
            yield self.head.value
        else:
            raise StopIteration
                 

if __name__ == '__main__':

    unlist = UnorderedList()
    unlist.add(20)
    unlist.add(30)
    unlist.add(50)
    unlist.add(40)
    print(unlist.size())
    print(unlist.search(20))
    print(unlist.search(300))
    unlist.remove(40)
    print(list(unlist))




