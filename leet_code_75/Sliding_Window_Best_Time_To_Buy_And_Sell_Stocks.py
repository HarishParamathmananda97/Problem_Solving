
""" 
Sliding Window: Best Time to Buy and Sell Stock - LeetCode 121 python.

Say you have an array for which ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e, buy one and sell one share of the stock), design an algorithm to find the maximum profit. 

Note that you cannot sell a stock before you buy one. 

Example1: 
Input: [7, 1, 5, 3, 6, 4]
Output: 5

Explanation: Buy on day2(price = 1) and sell on day 5(price = 6), profit 6 - 1 = 5. Not 7 - 1 = 6, as selling price needs to be larger than buying price.

"""


"""
Concept:
1st day - Left, 2nd day - Right,
buy when the first < second, else wait for it.
max profit by subtracting right and left
"""

class Solution:
    def __init__(self, input : list[int])->int:
        self.input = input

    def stock_market(self):
        print(self.input)
        left = 0
        right = 1
        maxProfit = 0

        while right < len(self.input):
            if self.input[left] > self.input[right]:
                left = right
            elif self.input[right] > self.input[left]:
                profit = self.input[right] - self.input[left]
                maxProfit = max(maxProfit, profit)
            right += 1
        return maxProfit


input = [7, 1, 5, 3, 6, 4, 2, 4, 5, 1, 8, 29]
input = [7, 1, 5, 3, 6, 4]
sol = Solution(input)
print(sol.stock_market())
