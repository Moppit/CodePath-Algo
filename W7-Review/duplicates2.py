# Suppose an array sorted in ascending order is rotated at 
# some pivot unknown to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
# 
# Example 1:
# 
# Input: [3,4,5,1,2] 
# Output: 1
# Example 2:
# 
# Input: [4,5,6,7,0,1,2]
# Output: 0

def findMin(nums):
  start = 0
  end = len(nums) - 1
  
  while start < end:
    mid = int((end+start) / 2)
    if mid == start or mid == end:
        break
    elif nums[mid] > nums[end]:
      start = mid
    else:
      end = mid
    
  return min(nums[start], nums[end])

a1 = [3, 4, 5, 1, 2]
a2 = [4, 5, 6, 7, 0, 1, 2]
a3 = [1, 2 ,3]
a4 = [1]
a5 = [4, 5, 6, 1]

print("Test 1 Passed: " + str(findMin(a1) == 1))
print("Test 2 Passed: " + str(findMin(a2) == 0))
print("Test 3 Passed: " + str(findMin(a3) == 1))
print("Test 4 Passed: " + str(findMin(a4) == 1))
print("Test 5 Passed: " + str(findMin(a5) == 1))