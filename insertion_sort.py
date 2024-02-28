

def insertion_sort(arr):
    #outer loop for iteration
    for i in range(1, len(arr)):
        # inner loop starts with the index of outer loop
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1] #swapping if index of j - 1 > index of j
            j -= 1 # moving to the left
            print(arr) 

if __name__ == '__main__':

    arr = input("Enter the numbers with space: ").split(' ')
    arr = list(map(int, arr))
    # print(arr)

    # arr = [2, 6, 5, 1, 3, 4]
    insertion_sort(arr)



""" 
Sample Input: 
[3, 7, 5, 1, 4, 2]
Sample Output: 
[3, 7, 5, 1, 4, 2]
[3, 5, 7, 1, 4, 2]
[3, 5, 1, 7, 4, 2]
[3, 1, 5, 7, 4, 2]
[1, 3, 5, 7, 4, 2]
[1, 3, 5, 4, 7, 2]
[1, 3, 4, 5, 7, 2]
[1, 3, 4, 5, 2, 7]
[1, 3, 4, 2, 5, 7]
[1, 3, 2, 4, 5, 7]
[1, 2, 3, 4, 5, 7]
"""