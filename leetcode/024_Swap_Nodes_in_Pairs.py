"""
24. Swap Nodes in Pairs


Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.



Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.


# https://leetcode.com/problems/swap-nodes-in-pairs/
# Given a linked list, swap every two adjacent nodes and return its head.
# E.g. given 1->2->3->4, you should return the list as 2->1->4->3.
# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

# Store the previous node, swap and append in pairs.
# Time - O(n)
# Space - O(1)


"""

class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def swap_pairs(self, head):


        prev = dummy = ListNode(None)


        while head and head.next:
            next_head = head.next.next
            prev.next = head.next
            head.next.next = head
            prev = head
            head = next_head

        prev.next = head
        return dummy.next

if __name__ == '__main__':

    s = Solution()
    root = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    root.next = two
    two.next = three
    three.next = four

    current =s.swap_pairs(root)


    #current = root
    while current is not None:
        print(current.val)
        current = current.next
