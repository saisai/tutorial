"""
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

# https://leetcode.com/problems/merge-two-sorted-lists/
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Whilst there are nodes in both lists, link to lowest head node and increment that list.  Finally link to
# the list with remaining nodes.
# Time - O(m+n)
# Space - O(1)


"""
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def merge_two_lists(self, l1, l2):

        prev = dummy = ListNode(None)    # new dummy head for merged list


        while l1 and l2:        # link prev to the lowest node

            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        prev.next = l1 or l2        # link prev to the list with remaining nodes
        return dummy.next

if __name__ == '__main__':

    l1 = ListNode(1)
    l12 = ListNode(2)
    l13 = ListNode(4)
    l1.next = l12
    l12.next = l13

    l2 = ListNode(1)
    l21 = ListNode(3)
    l22 = ListNode(4)
    l2.next = l21
    l21.next = l22

    s = Solution()
    s.merge_two_lists(l1, l2)

    while l2 is not None:
        print(l2.val)
        l2 = l2.next
