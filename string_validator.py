if __name__ == '__main__':
    s = input()
    # s = 'qA2'
    # s = '#$%@^&*'
    # print(s)
    alphanum = alpha = digit = lower = upper = 0
    for letter in s:
        if letter.isalnum():
            alphanum += 1
        if letter.isalpha():
            alpha += 1
        if letter.isdigit():
            digit += 1
        if letter.islower():
            lower += 1
        if letter.isupper():
            upper += 1
            
    if alphanum > 0:
        print(True)
    else:
        print(False)
    if alpha > 0:
        print(True)
    else:
        print(False)
    if digit > 0:
        print(True)
    else:
        print(False)
    if lower > 0:
        print(True)
    else:
        print(False)
    if upper > 0:
        print(True)
    else:
        print(False)
    
"""
Sample Input :
'qA2'
Sample Output : 
True
True
True
True
True

Sample Input2 :
'#$%@^&*'
Sample Output2:
False
False
False
False
False
"""