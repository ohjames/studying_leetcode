# Fast & Slow Pointers Pattern

## Key Concepts
- [Two pointers](two-pointers/two-pointers.md), one fast and one slow traversing data structure simultaneously.
- The pointers move until condition is met, typically reaching the end of a linked list or array, or finding a specific element.
- Use slow pointer to determine the desired result -- examples would be middle element of the linked list, the nth element from the end, or the point of intersection in a cycle.
- Commonly used in linked list problems to find middle element, detecting cycles, or checking for palindromes.
- Also used in array problems to finding duplicates or detecting cycle in an array.

## Benefits
- Efficient Time Complexity: The fast and slow pointers technique allows us to solve problems with a time complexity of O(N), where N is the number of elements in the linked list or array. This is because we only need to traverse the list or array once, using the two pointers.
- Space Efficiency: The fast and slow pointers pattern typically requires only a constant amount of extra space. This makes it a memory-efficient approach, especially when dealing with large data structures.

## Example Problems
1. LinkedList Cycle (easy) [Leetcode](https://leetcode.com/problems/linked-list-cycle/)
2. Start of LinkedList Cycle (medium) [Leetcode](https://leetcode.com/problems/linked-list-cycle-ii/)
3. Happy Number (medium) [Leetcode](https://leetcode.com/problems/happy-number/)
4. Middle of the LinkedList (easy) [Leetcode](https://leetcode.com/problems/middle-of-the-linked-list/)
5. Problem Challenge 1: Palindrome LinkedList (medium) [Leetcode](https://leetcode.com/problems/palindrome-linked-list/)
6. Problem Challenge 2: Rearrange a LinkedList (medium) [Leetcode](https://leetcode.com/problems/reorder-list/)
7. Problem Challenge 3: Cycle in a Circular Array (hard) [Leetcode](https://leetcode.com/problems/circular-array-loop/)