"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end, cnt = float('-inf'), 0
        for i in sorted(intervals, key=lambda x: x[1]):
            if i[0] >= end: 
                end = i[1]
            else: 
                cnt += 1
        return cnt
""" Broken thing I was working on:
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort all elements by start of interval -- keep shortest end first
        intervals.sort()
        count = 0
        kept = []
        for interval in intervals:
            if len(kept) == 0:
                kept.append(interval)
            else:
                toAdd = True
                for item in kept:
                    # If interval doesn't overlap with any, add - NOT FOOLPROOF
                    # If does, increment count
                    if interval[0] >= item[0] and interval[0] < item[1]:
                        count += 1
                        toAdd = False
                        break
                    elif interval[1] > item[0] and interval[1] <= item[1]:
                        count += 1
                        toAdd = False
                        break
                if toAdd:
                    kept.append(interval)
        return count
"""
