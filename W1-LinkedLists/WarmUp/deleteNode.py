"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Example:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

Notes:
The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # since we have to do this all in place, we can shift values I suppose
        temp = node
        while temp.next.next != None:
            temp.val = temp.next.val
            temp = temp.next
        temp.val = temp.next.val
        temp.next = None
