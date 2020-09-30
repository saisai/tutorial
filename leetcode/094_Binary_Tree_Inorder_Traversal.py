
'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Given a binary tree, return the inorder traversal of its nodes' values.
# Note: Recursive solution is trivial, could you do it iteratively?

# From root, go as far left as possible pushing all nodes onto stack. While nodes on stack, pop a node and add it to
# the result. Its left child (if any) has already been visited because it was added to the stack later so popped
# earlier. If the node has a right child, add that child and all its left branch to the stack.
# Time - O(n)
# Space - O(n)

'''

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorder_traversal(self, root):

        stack, result = [], []

        while root:     # make top of stack the smallest value
            stack.append(root)
            root = root.left

        print(root)

        while stack:

            node = stack.pop()
            result.append(node.val)

            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
        return result

if __name__ == '__main__':
    #inputs = [1, None,2,3]

    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    one.right = two
    two.left = three


    test = Solution()
    print(test.inorder_traversal(one))


