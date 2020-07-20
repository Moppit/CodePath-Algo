"""
Question: Given a string s , find the length of the longest substring t that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""
# Basic brute force strategy: nested loop
# Have a queue that contains the chars -- pop front, append to end
def longTwoCharSubStr(s):
    if len(s) <= 2:
        return len(s)
    longest = 0
    queue = []
    for char in s:
        if len(queue) > 2:
            char1 = queue[0]
            char2 = ""
            for item in queue:
                if item != char1:
                    char2 = item
                    break
            if char not in queue and char != char1 and char != char2:
                queue.pop(0)
            queue.append(char)
        else:
            queue.append(char)
        if len(queue) > longest:
            longest = len(queue)
    return longest

# Test cases:
print('T1. Input: "eceba", Expected Output: 3, Output:', longTwoCharSubStr("eceba"))
print('T2. Input: "aabbb", Expected Output: 5, Output:', longTwoCharSubStr("aabbb"))
print('T3. Input: "", Expected Output: 0, Output:', longTwoCharSubStr(""))
print('T4. Input: "a", Expected Output: 1, Output:', longTwoCharSubStr("a"))
print('T5. Input: "ohmmmmmmmmmmmmmho", Expected Output: 15, Output:', longTwoCharSubStr("hmmmmmmmmmmmmmh"))