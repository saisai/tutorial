"""

19. Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Given a linked list, remove the nth node from the end of list and return its head.

# Advance first pointer n steps then advance both pointers at same rate.
# Time - O(n)
# Space - O(1)

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def remove_nth_from_end(self, head, n):

        first, second = head, head

        for i in range(n):      # move first n steps forward
            first = first.next

        if not first:
            return head.next

        while first.next:   # move both pointers until first is at end
            first = first.next
            second = second.next

        second.next = second.next.next  # nth from end is second.next
        return head

if __name__ == '__main__':
    root = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    five = ListNode(5)
    root.next = two
    two.next = three
    three.next = four
    four.next = five

    s = Solution()
    s.remove_nth_from_end(root, 2)

    current = root
    while current is not None:
        print(current.val)
        current = current.next


