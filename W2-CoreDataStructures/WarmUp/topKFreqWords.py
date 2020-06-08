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

        # Pop out k items
        mostFreq = []
        for _ in range(k):
            if len(heap) == 1:
                freq, word = heappop(heap)
                mostFreq.append(word)
                break
            # Add all items of same freq as candidates, and then alphabetize
            candidates = []
            attempt = heappop(heap)
            candidates.append(attempt)
            while len(heap) != 0 and attempt[0] == heap[0][0]:
                candidates.append(heappop(heap))
            candidates.sort(key = lambda x: x[1])
            # Grab the first item and put the rest back in heap
            mostFreq.append(candidates[0][1])
            for i in range(1, len(candidates)):
                heappush(heap, candidates[i])
        return mostFreq
            
