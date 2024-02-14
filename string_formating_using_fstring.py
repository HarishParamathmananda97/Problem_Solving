#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
# Hello firstname lastname! You just delved into python

def print_full_name(first, last):
    # Write your code here
    print(f"Hello {first} {last}! You just delved into python.")
if __name__ == '__main__':
    first_name = input('Enter the first name: ')
    last_name = input('Enter the last name: ')
    print_full_name(first_name, last_name)


"""
Sample Input:
Enter the first name: Jerry
Enter the last name: Tom
Hello Jerry Tom! You just delved into python.

"""