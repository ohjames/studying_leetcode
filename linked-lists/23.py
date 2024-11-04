'''
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
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
'''

# https://leetcode.com/problems/merge-k-sorted-lists/

import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    def merge(l1, l2):
        dummy = ListNode()
        current = dummy
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 or l2
        return dummy.next

    if not lists:
        return None
    while len(lists) > 1:
        merged_lists = []
        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):
                merged_lists.append(merge(lists[i], lists[i + 1]))
            else:
                merged_lists.append(lists[i])
        lists = merged_lists
    return lists[0]

class TestMergeKLists(unittest.TestCase):
    def test1(self):
        l1 = ListNode(1, ListNode(4, ListNode(5)))
        l2 = ListNode(1, ListNode(3, ListNode(4)))
        l3 = ListNode(2, ListNode(6))
        result = mergeKLists([l1, l2, l3])
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 1)
        self.assertEqual(result.next.next.val, 2)
        self.assertEqual(result.next.next.next.val, 3)
        self.assertEqual(result.next.next.next.next.val, 4)
        self.assertEqual(result.next.next.next.next.next.val, 4)
        self.assertEqual(result.next.next.next.next.next.next.val, 5)
        self.assertEqual(result.next.next.next.next.next.next.next.val, 6)

    def test2(self):
        result = mergeKLists([])
        self.assertEqual(result, None)

    def test3(self):
        result = mergeKLists([None])
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()