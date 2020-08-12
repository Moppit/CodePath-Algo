"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
 

Constraints:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""
# Source: https://leetcode.com/problems/letter-case-permutation/discuss/115509/Python-simple-solution-(7-lines)
def letterCasePermutation(self, S):
    res = ['']
    for ch in S:
        if ch.isalpha():
            res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
        else:
            res = [i+ch for i in res]
    return res

""" Work so far:
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        wordSet = set(())
        lastVowel = 0
        wordSet.add(S)
        for i in range(len(S)):
            temp = S
            for j in range(lastVowel, len(temp)):
                if not temp[j].isnumeric():
                    lastVowel = i
                    if temp[j].upper() == temp[j]:
                        temp = temp[:j] + temp[j].lower() + temp[j+1:]
                    elif temp[j].lower() == temp[j]:
                        temp = temp[:j] + temp[j].upper() + temp[j+1:]
                    wordSet.add(temp)
                lastVowel += 1
        return list(wordSet)
"""