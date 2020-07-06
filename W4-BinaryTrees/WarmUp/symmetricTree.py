"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
"""
# What I had going:
"""
class Solution:
    
    def helper(self, queue, root: TreeNode):
        # If a leaf node, add to queue and stop traversing
        if root == None:
            return queue
        if root.left == None and root.right == None:
            queue += str(root.val)
            return queue
        # Deal with left branch (or if there isn't one)
        if root.left != None:
            queue = self.helper(queue, root.left)
        else:
            queue += '|'
        # Add root node value to queue (for left->curr->right, in order traversal)
        queue += str(root.val)
        # Deal with right branch (or if there isn't one)
        if root.right != None:
            queue = self.helper(queue, root.right)
        else:
            queue += '|'
        return queue
        
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = ""
        queue = self.helper(queue, root)
        print(queue)
        midpoint = len(queue)//2
        if ''.join(reversed(queue[0:midpoint])) != queue[len(queue)-midpoint:len(queue)]:
            return False
        return True
"""
# Test case it was failing:
"""
                    5
            4               1
        n       1       n       4
              2   n           2   n
"""
# Solution from discussion:
class Solution:
  def isSymmetric(self, root):
    if root is None:
      return True
    else:
      return self.isMirror(root.left, root.right)

  def isMirror(self, left, right):
    if left is None and right is None:
      return True
    if left is None or right is None:
      return False

    if left.val == right.val:
      outPair = self.isMirror(left.left, right.right)
      inPiar = self.isMirror(left.right, right.left)
      return outPair and inPiar
    else:
      return False
