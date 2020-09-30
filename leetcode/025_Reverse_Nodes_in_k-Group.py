"""
25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.


# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
# You may not alter the values in the nodes, only nodes itself may be changed.
# Only constant memory is allowed.

# If there are at least k nodes, recursively reverse remainder and append reversed group to reversed remainder.
# Time - O(n)
# Space - O(1)

"""

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        if k < 2:
            return head

        node = head
        for _ in range(k):
            if not node:
                return head   # return head if there are not at least k nodes
            node = node.next
        # else node is now head of second group

        # reverse remainder after this group
        prev = self.reverseKGroup(node, k)

        for _ in range(k):  # reverse this group, adding in front of prev
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev

if __name__ == '__main__':

    root = ListNode(1)
    r2 = ListNode(2)
    r3 = ListNode(3)
    r4 = ListNode(4)
    r5 = ListNode(5)

    root.next = r2
    r2.next = r3
    r3.next = r4
    r4.next = r5
    s = Solution()
    r = s.reverseKGroup(root, 2)

    rr = root
    while rr is not None:
        print(rr.val)
        rr = rr.next

    print('*' * 100)
    current = r
    while current is not None:
        print(current.val)
        current = current.next
