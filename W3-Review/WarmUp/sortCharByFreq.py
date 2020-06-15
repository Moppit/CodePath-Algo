"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        # Yeet everything into a dictionary
        if len(s) == 0:
            return s
        dictionary = {}
        for char in s:
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1
        # Put in a heap and create final string
        heap = []
        for char in dictionary:
            heapq.heappush(heap, (-1*dictionary[char], char))
        # Create a final string that is the key * number times it appears
        to_return = ""
        while len(heap) > 0:
            item = heapq.heappop(heap)
            to_return += -1*item[0]*item[1]
        # return string
        return to_return