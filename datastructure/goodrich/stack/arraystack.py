from exception import Empty

class ArrayStack:
    """
    LIFO Stack implementation using a Python list as underlying storage.
    """

    def __init__(self):
        """Create an empty statck."""
        self._data = []

    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack"""
        self._data.append(e)

    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        """
        Remove and return the element from the top of the stack (i.e LIFO).

        Raise Empty exception if the stack is empty.
        """

        if self.is_empty():
            raise Empty('Stack is empty')

        return self._data.pop()     # remove last item from list

if __name__ == "__main__":
    S = ArrayStack()

    S.push(5)
    S.push(3)
    print(len(S))
    print(S.top())
    print(S.pop())
    print(S.is_empty())
    print(S.pop())
    try:
        print(S.pop())
    except Empty as e:
        print(e)
    print(len(S))

