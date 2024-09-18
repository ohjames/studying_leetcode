'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: [] 

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 
Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# https://leetcode.com/problems/reverse-linked-list/

import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev

class TestReverseLinkedList(unittest.TestCase):
    def list_to_string(self, head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values

    def assertLinkedListEqual(self, head1, head2):
        self.assertEqual(self.list_to_string(head1), self.list_to_string(head2))

    def test_example1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        expected = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
        result = reverse_list(head)
        self.assertLinkedListEqual(result, expected)

    def test_example2(self):
        head = ListNode(1, ListNode(2))
        expected = ListNode(2, ListNode(1))
        result = reverse_list(head)
        self.assertLinkedListEqual(result, expected)

    def test_example3(self):
        head = None
        expected = None
        result = reverse_list(head)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()