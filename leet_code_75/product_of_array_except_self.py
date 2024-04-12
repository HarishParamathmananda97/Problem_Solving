# Product of array except self

"""
sample :
input: nums = [1,2,3,4]
output: [24, 12, 8, 6]
catch: write algorithm that runs in O(n) time and without using the division operator
"""

class Solution:
    def productionExceptSelf(self, nums):
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
    
nums = [1, 2, 3, 4, 5]
sol = Solution()
result = sol.productionExceptSelf(nums)
print(result)