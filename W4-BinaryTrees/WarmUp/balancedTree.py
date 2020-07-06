"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

Link to correct solution: https://leetcode.com/problems/balanced-binary-tree/discuss/35708/VERY-SIMPLE-Python-solutions-(iterative-and-recursive)-both-beat-90

"""
class Solution(object):
    def isBalanced(self, root):
            
        def check(root):
            if root is None:
                return 0
            left  = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
            
        return check(root) != -1

# 226 / 226 test cases passed.
# Status: Accepted
# Runtime: 80 ms

# What I had going that was failing the last few test cases:
"""
    def helper(self, root: TreeNode, height, storeHeights):    
        # If none, add to storeHeights and return
        if root is None:
            storeHeights.append(height)
            return height, storeHeights
        # Else, add one to height and return
        else:
            height += 1
            leftHeight, leftStore = self.helper(root.left, height, storeHeights)
            rightHeight, rightStore = self.helper(root.right, height, storeHeights)
            storeHeights = leftStore + rightStore
            return height, storeHeights
            

    def isBalanced(self, root: TreeNode) -> bool:
        _, heights = self.helper(root, 0, [])
        high = max(heights, default=0)
        low = min(heights, default=0)
        print('high:', high, 'low:', low)
        return (high-low) < 2
"""
# Failed at this test case:
"""
                                    1
                        2                       2
                3               3       3               3
            4       4       4     4   4     4       n       n
          5   5
"""
