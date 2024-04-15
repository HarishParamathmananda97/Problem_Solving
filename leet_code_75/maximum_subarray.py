# Maximum Sub Array - Kadane's algorithm

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


class Solution:
    def maxSubArray(self, arr):
        return self.maxSubArrayHelper(arr, 0, len(arr) - 1)
    
    def maxSubArrayHelper(self, arr, left, right):
        if left == right:
            return arr[left]
        
        mid = (left + right) // 2
        
        # Find maximum subarray sum in left half, right half, and across the midpoint
        left_max = self.maxSubArrayHelper(arr, left, mid)
        right_max = self.maxSubArrayHelper(arr, mid + 1, right)
        cross_max = self.maxCrossingSubArray(arr, left, mid, right)
        
        # Return the maximum of the three sums
        return max(left_max, right_max, cross_max)
    
    def maxCrossingSubArray(self, arr, left, mid, right):
        # Find maximum sum of subarray crossing the midpoint
        left_sum = float('-inf')
        cur_sum = 0
        for i in range(mid, left - 1, -1):
            cur_sum += arr[i]
            left_sum = max(left_sum, cur_sum)
        
        right_sum = float('-inf')
        cur_sum = 0
        for i in range(mid + 1, right + 1):
            cur_sum += arr[i]
            right_sum = max(right_sum, cur_sum)
        
        return left_sum + right_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sol = Solution()
num = sol.maxSubArray(arr)
print(num)

