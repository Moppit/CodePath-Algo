"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return permutations(nums)