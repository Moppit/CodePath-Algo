"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example:
Input: s = "paper", t = "title"
Output: true
"""

# FYI, this solution is super slow and should be optimized at some point
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Fundamentally, need to determine whether letters are different from all the others, and whether they are a duplicate
        
        So, can create a hash table: array with 26 slots containing boolean values
        OR, for an easier implementation, just store whether they're in the list
        -> For both, iterate through the strings (same length) and determine if they have a duplicate or not a duplicate... would have to check the element index in the list though, have to be in the same order
        
        Ex.
        s = "egg", t = "add"
        sQueue = []
        tQueue = []
        
        1. Not in? Yes. sQueue = ['e'], tQueue = ['t']
        2. Not in? Yes. sQueue = ['e', 'g'], tQueue = ['a', 'd']
        3. Not in? No. Index match? 1 == 1, so yes. sQueue = ['e', 'g'], tQueue = ['a', 'd']
        
        If in any case, one of these 3 isn't true, then return false
        
        There's probably a better way to do this where you use character properties 
        to determine whether letters are in the right spot, but need to think about
        that hash function very carefully.
        """
        sQueue = []
        tQueue = []
        for i in range(len(s)):
            if s[i] not in sQueue and t[i] not in tQueue:
                sQueue.append(s[i])
                tQueue.append(t[i])
            elif s[i] in sQueue and t[i] in tQueue:
                if sQueue.index(s[i]) != tQueue.index(t[i]):
                    return False
            else:
                return False
        return True
                
