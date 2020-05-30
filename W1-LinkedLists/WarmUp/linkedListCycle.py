"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        items = []
        temp = head
        while temp != None:
            # Originally did this with .val, but only works for unique vals
            # So switched to checking addresses instead, even tho slow
            if temp in items:
                return True
            else:
                items.append(temp)
            temp = temp.next
        return False
