"""
Input: [3, 4, 5, 1, 2]
Output: 
Time Complexity : O(log n)

Binary search
"""


 #[3, 4, 5, 1, 2] -> m > l 5 >= 3 l = 2 + 1= 3, r = 4 nums[3] < nums[4] - 1 < 2 = min(res, nums[l]) = res
class Solution:
    def findMin(self, nums :list[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) -1
        
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
                
            m = (l + r)//2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res


arr = [3, 4, 5, 1, 2]
sol = Solution()
result = sol.findMin(arr)
print(result)
