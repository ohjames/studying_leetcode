# Merging Intervals

The merging intervals pattern is a common algorithmic pattern used to merge overlapping intervals. It is often used in scenarios where we need to find the overlapping intervals and merge them into a single interval.

## Approach

To solve problems using the merging intervals pattern, we can follow these steps:

1. Sort the intervals based on their start time.
2. Initialize an empty result list to store the merged intervals.
3. Iterate through the sorted intervals:
    - If the current interval does not overlap with the previous interval, add it to the result list.
    - If the current interval overlaps with the previous interval, merge them by updating the end time of the previous interval.
4. Return the result list containing the merged intervals.

## Example

Let's consider an example to understand how the merging intervals pattern works:

Given the intervals: [[1, 3], [2, 6], [8, 10], [15, 18]]

After sorting the intervals based on their start time, we get: [[1, 3], [2, 6], [8, 10], [15, 18]]

Iterating through the sorted intervals:

- The first interval [1, 3] does not overlap with the previous interval, so we add it to the result list.
- The second interval [2, 6] overlaps with the previous interval [1, 3], so we merge them into [1, 6].
- The third interval [8, 10] does not overlap with the previous interval [1, 6], so we add it to the result list.
- The fourth interval [15, 18] does not overlap with the previous interval [8, 10], so we add it to the result list.

The final merged intervals are: [[1, 6], [8, 10], [15, 18]]

## Conclusion

The merging intervals pattern is a useful technique for merging overlapping intervals. By following the approach mentioned above, we can efficiently merge intervals and solve related problems.