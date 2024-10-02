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

def merge_k_sorted_lists(lists):
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]
    mid = len(lists) // 2
    left = merge_k_sorted_lists(lists[:mid])
    right = merge_k_sorted_lists(lists[mid:])
    return merge_two_sorted_lists(left, right)

def merge_two_sorted_lists(l1, l2):
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

class TestMergeKSortedLists(unittest.TestCase):
    def list_to_string(self, head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values

    def assertLinkedListEqual(self, head1, head2):
        self.assertEqual(self.list_to_string(head1), self.list_to_string(head2))

    def test_example1(self):
        lists = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
        expected = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6))))))))
        result = merge_k_sorted_lists(lists)
        self.assertLinkedListEqual(result, expected)

    def test_example2(self):
        lists = []
        expected = None
        result = merge_k_sorted_lists(lists)
        self.assertLinkedListEqual(result, expected)

    def test_example3(self):
        lists = [None]
        expected = None
        result = merge_k_sorted_lists(lists)
        self.assertLinkedListEqual(result, expected)

if __name__ == '__main__':
    unittest.main()