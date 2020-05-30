"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Constraints
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
The length of the linked list is between [0, 10^4].
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # Keep track of prev, curr, and index
        """
        Basically chain all your items to next next and then depending on whether your end index is odd or even, append one chain to another
        Store the first and second node pointers
        Store the second to last and last pointers
        """
        if head == None or head.next == None:
            return head
        
        oddHead = head
        evenHead = head.next
        temp = head
        index = 1
        # Only iterate to the third to last node (leave two at the end)
        while temp.next.next != None:
            temp2 = temp.next
            temp.next = temp.next.next
            temp = temp2
            index += 1
        # Append the chains: find last odd element, and make next the evenHead
        if index % 2 == 0:  # Odd length chain, bc index iterated one more time
            # We know temp is currently at second to last element, so last element is odd
            temp.next.next = evenHead
            # If list elements even, all good. if odd, need to make last node empty
            temp.next = None
        else:
            temp.next = evenHead
        
        return oddHead
