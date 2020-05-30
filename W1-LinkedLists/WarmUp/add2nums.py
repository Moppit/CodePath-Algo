"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Append each into a string and then add them
        # Can't assume they are the same length
        num1 = ""
        num2 = ""
        temp1 = l1
        temp2 = l2
        while(temp1 != None or temp2 != None):
            # Deal with l1
            if temp1 != None:
                num1 = str(temp1.val) + num1
                temp1 = temp1.next
            if temp2 != None:
                num2 = str(temp2.val) + num2
                temp2 = temp2.next

        # now create a new list
        newVal = str(int(num1) + int(num2))
        newVal = ''.join(reversed(newVal))
        newList = ListNode(val=int(newVal[0]), next=None)
        temp = newList
        for i in range(1,len(newVal)):
            newNode = ListNode(val=int(newVal[i]), next=None)
            temp.next = newNode
            temp = newNode
        return newList
