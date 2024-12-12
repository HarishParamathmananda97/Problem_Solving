"""
Finding median of the array.
sample input = [0, 1, 4, 5, 3, 2, 6,8]

sample output = 
"""

def median_finding(arr):
    arr.sort()
    n = len(arr)
    print(n)
    if n % 2 != 0:
        return arr[n//2]
    return float(arr[n//2] + arr[(n-1)//2])

arr = [0, 1, 4, 5, 3, 2, 6, 8]
res = median_finding(arr)
print(res)

def median_finding(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    
    if n % 2 != 0:
        return sorted_arr[n // 2]
    else:
        middle_right = sorted_arr[n // 2]
        middle_left = sorted_arr[(n // 2) - 1]
        return (middle_right + middle_left) / 2

arr = [0, 1, 4, 5, 3, 2, 6, 8]
res = median_finding(arr)
print(res)

