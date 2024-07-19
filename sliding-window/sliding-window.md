## Sliding Window Pattern

## Key Concepts
- [Two pointers](two-pointers/two-pointers.md) approach to maintain window boundaries -- the pointers help efficiently moving the window and processing elements.
- Size of window detmines the number of elements considered at a time -- can be fixed or variable.
- Window moves by incrementing or decrementing (aka window can expand or shrink) its boundaries based on specific conditions, allowing us to process the elements efficiently.

## Benefits
- Time Efficiency: Sliding window pattern often provides optimized solution by reducing time complexity from O(n^2) to O(n).
- Versatility: Can be applied to subarrays, substring problems, or solving optimization problems.

## Example Problems
1. Maximum Sum Subarray of Size K (easy)
2. Smallest Subarray with a given sum (easy) [Educative.io](https://www.educative.io/courses/grokking-the-coding-interview/7XMlMEQPnnQ)
3. Longest Substring with K Distinct Characters (medium) [Educative.io](https://www.educative.io/courses/grokking-the-coding-interview/YQQwQMWLx80)
4. Fruits into Baskets (medium) [LeetCode](https://leetcode.com/problems/fruit-into-baskets/)
5. No-repeat Substring (hard) [LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
6. Longest Substring with Same Letters after Replacement (hard) [LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/)
7. Longest Subarray with Ones after Replacement (hard) [LeetCode](https://leetcode.com/problems/max-consecutive-ones-iii/)
8. Problem Challenge 1: Permutation in a String (hard) [Leetcode](https://leetcode.com/problems/permutation-in-string/)
9. Problem Challenge 2: String Anagrams (hard) [Leetcode](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
10. Problem Challenge 3: Smallest Window containing Substring (hard) [Leetcode](https://leetcode.com/problems/minimum-window-substring/)
11. Problem Challenge 4: Words Concatenation (hard) [Leetcode](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)