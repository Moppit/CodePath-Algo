"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # check where item is relative to last item in list
        for row in matrix:
            if len(row) == 0:
                return False
            if target <= row[len(row)-1]:
                if target in row:
                    return True
                return False
        # If get to the end, return false
        return False