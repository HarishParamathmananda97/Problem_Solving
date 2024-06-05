nums = list(map(int, '5 3 8 6 7 2'.split(' ')))
print(nums)

for i in range(len(nums)-1, 0, -1):
    for j in range(i):
        if nums[j] > nums[j+1]:
            print("before : nums[i], nums[j] is: ",nums[i], nums[j])
            nums[j], nums[i] = nums[i], nums[j]
            print("after : nums[i], nums[j] is: ",nums[i], nums[j])

    

print(nums)

print("sUccess depends on second letter. -SteveJobs.")