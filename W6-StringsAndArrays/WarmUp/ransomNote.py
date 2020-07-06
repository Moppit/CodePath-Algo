"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

You may assume that both strings contain only lowercase letters.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Put all of magazine in a dictionary
        dictionary = {}
        for val in magazine:
            if val not in dictionary:
                dictionary[val] = 1
            else:
                dictionary[val] += 1
        # Go thru each letter in ransomNote
        for letter in ransomNote:
            # If not a key in dictionary, return false
            if letter not in dictionary:
                return False
            # Else if val at key is 0, return false
            elif dictionary[letter] == 0:
                return False
            # Else val at key is decremented by 1
            else:
                dictionary[letter] -= 1
        # Return true
        return True