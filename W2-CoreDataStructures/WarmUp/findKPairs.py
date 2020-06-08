"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence: 
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
"""

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        willReturn = []
        allPairs = {}
        allKeys = []
        # find all combos
        for first in nums1:
            for second in nums2:
                s = first + second
                if str(s) not in allPairs:
                    allPairs[str(s)] = [[first, second]]
                    allKeys.append(s)
                else:
                    allPairs[str(s)].append([first, second])
        # Sort allKeys
        allKeys.sort()
        numFound = 0
        # Then add pairs to willReturn until either allKeys is empty or k is met
        while len(allKeys) > 0 and numFound < k:
            # Get top item off of keys
            lowestSum = allKeys[0]
            listToEval = allPairs[str(lowestSum)]
            if len(listToEval) > 0:
                willReturn.append(listToEval.pop(0))
                numFound += 1
            else:
                allKeys.pop(0)
        return willReturn
