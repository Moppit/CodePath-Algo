"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""
# Valid, but has an excessively long run time for some cases
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        output = []
        maximum = max(T)
        while len(T) != 0:
            idx = 0
            if T[0] != maximum:   
                for i in range(len(T)):
                    if i != 0 and T[i] > T[0]:
                        idx = i
                        break
            output.append(idx)
            prev = T[0]
            T.pop(0)
        return output

"""         A Much Better Solution that you found in discussion, unfortunately
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
            # Initialize anticipated values to 0, to account for edge cases
            res = [0] * len(T)
            # Stack stores item indices
            stack = []

            # Iterate backward for each element before the end element
            for index in range(len(T)-1, -1, -1):
                # Iterate while there are items in the stack and the item at the last stack item's idx is less than the current item
                while stack and T[stack[-1]] <= T[index]:
                    # If less, pop off the item bc it's not useful to us
                    stack.pop()

                # Once you find a greater item or there's nothing left, calc the distance
                res[index] = stack[-1] - index if stack else 0
                # Add index to stack
                stack.append(index)

            return res
"""