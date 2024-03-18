
"""
Find the first sum of two numbers which met the target value.
"""
#BruteForce Method:

Input = [2, 1, 5, 3]
# need to find sum of two numbers equals to Target
Target = 4

for index in range(len(Input)): 
    for num1 in range(index + 1, len(Input)):
        if (Input[index] + Input[num1]) == Target:
            print(index, num1)
            break

print("success")
#Time Complexity: O(n^2)

#logically solved:
found_index = {}
for index, input_num in  enumerate(Input):
    val = Target - input_num
    if val in found_index:
        print(index, found_index[val])
        print("success")

    else:
        found_index[input_num] = index

#Time Complexity: O(n)
"""
Sample Input: [2,1,5,3]
Target: 4
Sample Output: [1, 3]"""