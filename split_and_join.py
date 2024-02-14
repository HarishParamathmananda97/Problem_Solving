def split_and_join(line):
    # write your code here
    str_join = line.split(' ')
    str_join = '-'.join(str_join)
    return str_join
    
if __name__ == '__main__':
    line = input("Enter the string with spaces: ")
    result = split_and_join(line)
    print(result)



"""
Enter the string with spaces: Welcome to Jerry World!
Welcome-to-Jerry-World!
"""