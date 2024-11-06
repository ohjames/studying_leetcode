'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 
Constraints:
The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
'''

# https://leetcode.com/problems/reorder-list/

import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    if not head:
        return None
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev = None
    curr = slow
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    first = head
    second = prev
    while second.next:
        temp = first.next
        first.next = second
        first = temp
        temp = second.next
        second.next = first
        second = temp
    return head

class TestReorderList(unittest.TestCase):
    def test1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        result = reorderList(head)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 4)
        self.assertEqual(result.next.next.val, 2)
        self.assertEqual(result.next.next.next.val, 3)

    def test2(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        result = reorderList(head)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 5)
        self.assertEqual(result.next.next.val, 2)
        self.assertEqual(result.next.next.next.val, 4)
        self.assertEqual(result.next.next.next.next.val, 3)

if __name__ == '__main__':
    unittest.main()