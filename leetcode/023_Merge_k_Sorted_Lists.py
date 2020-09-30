"""

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.

# https://leetcode.com/problems/merge-k-sorted-lists/
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Maintain a min heap of tuples of (val, list index) for the next node in each list.
# Also maintain a list of the next node to be merged for each list index.
# Time - O(n log k) for n total nodes, each of which is pushed and popped from heap in log k time.
# Space - O(k) for heap of k nodes

"""
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

import heapq

class Solution:

    def merge_k_lists(self, lists):

        prev = dummy = ListNode(None)
        next_nodes, heap = [], []

        for i, node in enumerate(lists):
            next_nodes.append(node)     # next_nodes[i] is the next node to be merged from lists[i]
            if node:
                heap.append((node.val, i))
        heapq.heapify(heap)


        while heap:
            value, i = heapq.append(heap)
            node = next_nodes[i]
            prev.next = node        # add node to merged list
            prev = prev.next
            if node.next:
                next_nodes[i] = node.next
                heapq.heappush(heap, (node.next.val, i))

        return dummy.next

if __name__ == "__main__":
    s = Solution()
    lists = [[1,4,5],[1,3,4],[2,6]]
    print(s.merge_k_lists(lists))
