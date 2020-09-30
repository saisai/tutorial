
from tree import BinaryTree


class Solution(object):

    def is_same_tree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False

        if p.x != q.x:
            return False
        return self.is_same_tree(p.left, q.left) \
            and self.is_same_tree(p.right, q.right)

if __name__ == '__main__':

    p = BinaryTree(1)
    p.insert_left(2)
    p.insert_right(3)

    q = BinaryTree(1)
    p.insert_left(2)
    p.insert_right(3)

    t = Solution()
    print(t.is_same_tree(p, q))

