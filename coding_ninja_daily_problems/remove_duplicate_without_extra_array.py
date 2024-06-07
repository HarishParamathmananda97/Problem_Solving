def removeDuplicates(arr,n):
    # Write your code here.
    count = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[count]:
            count += 1
            arr[count] = arr[i]
    return count + 1



n = 5
arr = [ 1, 2, 2, 2, 3 ]
removeDuplicates(arr, n)
"""
sample input = [1, 2, 2, 2, 3]
sample output = 3

"""
