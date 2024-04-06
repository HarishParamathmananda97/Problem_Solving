"""
Summary: 
Given an integer array nums, returns true if any value appears at least twice in the array, and returns false if every element is distinct.

Example1: 
Input: nums = [1, 2, 3, 1]
Output: True

Example 2:
Input: nums = [1, 2, 3, 4]
Output: False

Example 3:
Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: True
"""
user_inputs = [[1,2,3,1],[1,2,3,4],[1,1,1,3,3,4,3,2,4,2]]

# alternative methods: 
# 1) Brute force
#input; 1, 1, 1, 3, 3, 4, 3, 2, 4, 2
def Solution(input):
    for i in range(len(input)):
        for j in range(len(input[1:i])):
            if input[i] == input[j]:
                return True
    
    return False

for input in user_inputs:
    print(Solution(input))
        

# 2) sorting

def Solution(input):
    input.sort()
    first_num = input[0]
    for num in input[1:]:
        if num == first_num:
            return True
        else:
            first_num = num
    return False

for input in user_inputs:
    print(Solution(input))
    
# 3) hashmapping
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        # print(hashset)

        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False
    
sol = Solution()
for input in user_inputs:
    print(sol.containsDuplicate(input))

# 4) converting list to set to remove duplicate and then check the length 
def Solution(input):
    result = set(input)
    if len(input) == len(result):
        return 'false'
    else:
        return 'true'
        

for input in user_inputs:
    print(Solution(input))