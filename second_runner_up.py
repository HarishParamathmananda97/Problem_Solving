"""
To get the second Runner, ignore the first by sorting the list in reverse order and skip the first to get the second one. 
"""


if __name__ == '__main__':
    # n = int(input())
    # arr = list(map(int, input().split()))
    arr = [2,3,6,6,5]
    arr.sort(reverse= True)
    first = arr[0]
    for runner in arr[1:]:
        if runner != first:
            print(runner)
            break
    



"""
input: 5
6 3 2 3 5
arr = [6, 3, 2, 3, 5]
output: 5
"""
    