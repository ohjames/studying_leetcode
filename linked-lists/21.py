'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

# https://leetcode.com/problems/merge-two-sorted-lists/

import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
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

class TestMergeTwoLists(unittest.TestCase):
    def test1(self):
        l1 = ListNode(1, ListNode(2, ListNode(4)))
        l2 = ListNode(1, ListNode(3, ListNode(4)))
        result = mergeTwoLists(l1, l2)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 1)
        self.assertEqual(result.next.next.val, 2)
        self.assertEqual(result.next.next.next.val, 3)
        self.assertEqual(result.next.next.next.next.val, 4)
        self.assertEqual(result.next.next.next.next.next.val, 4)

    def test2(self):
        l1 = None
        l2 = None
        result = mergeTwoLists(l1, l2)
        self.assertEqual(result, None)

    def test3(self):
        l1 = None
        l2 = ListNode(0)
        result = mergeTwoLists(l1, l2)
        self.assertEqual(result.val, 0)

if __name__ == '__main__':
    unittest.main()