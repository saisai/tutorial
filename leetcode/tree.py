class BinaryTree:

    def __init__(self, x):
        self. x = x
        self.left = None
        self.right = None

    def insert_left(self, x):
        if self.left == None:
            self.left = BinaryTree(x)
        else:
            t = BinaryTree(x)
            t.left = self.left
            self.left = t

    def insert_right(self, x):
        if self.right == None:
            self.right = BinaryTree(x)
        else:
            t = BinaryTree(x)
            t.right = self.right
            self.right = t

    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left

    def set_root_value(self, x):
        self.x = x

    def get_root_value(self):
        return self.x



if __name__ == '__main__':
    r = BinaryTree('a')
    print(r.get_root_value())
    print(r.get_left_child())
    r.insert_left('b')
    print(r.get_left_child())
    print(r.get_left_child().get_root_value())



    # https://runestone.academy/runestone/books/published/pythonds/Trees/NodesandReferences.html
