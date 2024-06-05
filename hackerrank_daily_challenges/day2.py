"""
Finding the repetation of substring in the given string"""
def count_substring(string, sub_string):
    count = 0
    for index in range(0, len(string)-1):
        r = string[index : index + len(sub_string)]
        print(sub_string, r)
        if sub_string == r:
            count+= 1
    return count

if __name__ == '__main__':
    # string = input().strip()
    # sub_string = input().strip()
    string = 'ABCDCDC'
    sub_string = 'CDC'
    count = count_substring(string, sub_string)
    print(count)