"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.


# https://leetcode.com/problems/add-two-numbers/
# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# Iterate over lists. Add to result a node with the the sum of input nodes plus carry, mod 10.
# Time - O(max(m,n)) where m and n are input list lengths.
# Space - O(max(m,n)), output will be at most one digit more than longest input.


"""
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def add_two_numbers(self, l1, l2):
        prev = result = ListNode(None)
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            prev.next = ListNode(carry % 10)
            prev = prev.next
            carry //= 10
        return result.next


if __name__ == '__main__':
    l1 = ListNode(2)
    a = ListNode(4)
    b = ListNode(3)
    l1.next = a
    a.next = b


    l2 = ListNode(5)
    aa =ListNode(6)
    bb = ListNode(4)
    l2.next = aa
    aa.next = bb

    t = Solution()
    current = t.add_two_numbers(l1, l2)

    while current != None:
        print(current.val, '-> ', end='')
        current = current.next


