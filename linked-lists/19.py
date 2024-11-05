'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Follow up: Could you do this in one pass?
'''

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    slow = fast = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next

class TestRemoveNthFromEnd(unittest.TestCase):
    def test1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        result = removeNthFromEnd(head, 2)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 3)
        self.assertEqual(result.next.next.next.val, 5)

    def test2(self):
        head = ListNode(1)
        result = removeNthFromEnd(head, 1)
        self.assertIsNone(result)

    def test3(self):
        head = ListNode(1, ListNode(2))
        result = removeNthFromEnd(head, 1)
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.next)

if __name__ == '__main__':
    unittest.main()