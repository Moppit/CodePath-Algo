"""
Reverse singly linked list

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Strategy: make next pointer point to prev element - save next in temp
        if head == None or head.next == None:
            return head
        # If longer than 1 element
        prev = None
        temp = head
        while temp != None:
            future = temp.next
            temp.next = prev
            prev = temp
            temp = future
        return prev
        
