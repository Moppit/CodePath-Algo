"""
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
"""

import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Figure out frequencies [O(n) extra space, O(n) time]
        words.sort()
        storage = {}
        for elem in words:
            if elem in storage:
                storage[elem] -= 1
            else:
                storage[elem] = -1
        # Yeet it all into a heap based on the counts
        heap = []
        for item in storage:
            heappush(heap, (storage[item], item))
        # Pop k items out of the heap
        returnable = []
        for _ in range(k):
            freq, word = heappop(heap)
            returnable.append(word)
        return returnable
