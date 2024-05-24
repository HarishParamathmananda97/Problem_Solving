# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.

Sample Input: 
3 2 #m n
1 5 3 # n
3 1 # A
5 7 # B

Sample Output:
1

"""

if __name__ == '__main__':
    n, m = map(int, input().split(' '))
    n_num = list(map(int, input().split(' ')))
    a_like = set(map(int, input().split(' ')))
    b_dislike = set(map(int, input().split(' ')))
    
    total_happiness = 0
    for _num in n_num:
        # print(_num)
        if _num in a_like:
            total_happiness += 1
        if _num in b_dislike:
            total_happiness -= 1
            
    print(total_happiness)