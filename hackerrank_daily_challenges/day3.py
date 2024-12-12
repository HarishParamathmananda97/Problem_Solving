# Enter your code here. Read input from STDIN. Print output to STDOUT
def palindrome_integer(num):
    # num = 111
    rev_str = []
    while num > 0:
        last_digit = num % 10
        num = num // 10
        rev_str.append(str(last_digit))
    after_str = rev_str[::-1]
    if ''.join(rev_str) == ''.join(after_str):
        return True
    return False
    
num = input()
inp = list(map(int, input().split(' ')))

print(all([True if n > 0 else False for n in inp]) and any([palindrome_integer(num) for num in inp]))

"""
sample Input: 
5
12 9 61 5 14 
sample Output:
True

sample Input2: 
6
12 9 61 5 14 -26
sample Output2:
False


sample Input3: 
1
81
sample Output3:
False
"""