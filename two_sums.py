# arr = [13, 5, 7, 2, 8, 11]
# target = 9


# for num in range(len(arr)):
#     for j in range(num + 1, len(arr) ):
#         if target == arr[num] + arr[j]:
#             print(num, j)

def two_sums_solution(arr, target):
    # a + b = target
    # a = target - b
    found_nums = {}
    for index, num in enumerate(arr):
        result = target - num
        if num in found_nums:
            return (index, found_nums[num])
        found_nums[result] = index 
    return None



arr = [13, 5, 7, 2, 8, 11, 22]
target = 12
print(two_sums_solution(arr, target))



