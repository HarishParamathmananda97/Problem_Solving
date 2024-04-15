# Maximum Sub Array

"""
Question: Given an Integer array nums, find the contiguous subarray containing at least one number) which has the largest sum and return its sum.

Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4],
Output: 6
Explanation: [4, -1, 2, 1] has the largest sum = 6
"""

class Solution:
    def maxSub(self, arr):
        cur_sum = 0
        max_sum = float('-inf')
        n = len(arr)

        for i in range(n):
            cur_sum += arr[i] 
            max_sum = max(max_sum, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        return max_sum 
            

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sol = Solution()
num = sol.maxSub(arr)
print(num)