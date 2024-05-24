# # Enter your code here. Read input from STDIN. Print output to STDOUT
str = input()
"""
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
"""
# # we are going to follow segregation method, then joining them all

lowercase_letters = [char for char in str if char.islower()]
lowercase_letters.sort()
uppercase_letters = [char for char in str if char.isupper()]
uppercase_letters.sort()
numeric_characters = [char for char in str if char.isdigit()]
numeric_characters.sort(key=lambda x: int(x) % 2 == 0)
# print(lowercase_letters, uppercase_letters, numeric_characters)
print(''.join(lowercase_letters)+''.join(uppercase_letters)+''.join(numeric_characters))

# Read input from STDIN
input_str = input()

# Extract and sort lowercase letters
lowercase_letters = sorted([char for char in input_str if char.islower()])

# Extract and sort uppercase letters
uppercase_letters = sorted([char for char in input_str if char.isupper()])

# Extract numeric characters
odd_digits = sorted([char for char in input_str if char.isdigit() and int(char) % 2 != 0])
even_digits = sorted([char for char in input_str if char.isdigit() and int(char) % 2 == 0])

# Concatenate the sorted segments and print the result
sorted_str = ''.join(lowercase_letters) + ''.join(uppercase_letters) + ''.join(odd_digits) + ''.join(even_digits)
print(sorted_str)


"""
sample input:
1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0pQWERTYUIOPASDFGHJKLZXCVBNM
sample output:
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468
"""