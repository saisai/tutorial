from unordered_list import Node, UnorderedList


class OrderedList(UnorderedList):

    def __init__(self):
        super().__init__()

    def search(self, item):
        current = self.head

        while current is not None:
            if current.value == item:
                return True
            if current.value > item:
                return False
            current = current.next
        return False

    def add(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.value > item:
                break
            previous, current = current, current.next

        temp = Node(item)
        if previous is None:
            temp.next, self.head = self.head, temp
        else:
            temp.next, previous.next = current, temp
            
    
    def __iter__(self):
        return self 
        
    def __next__(self):   
        while current is not None:
            if current is None:
                raise StopIteration
            yield current.value 
            current = current.next
       
            


if __name__ == '__main__':

    ordered = OrderedList()
    ordered.add(30)
    ordered.add(40)
    
    print(list(ordered))
