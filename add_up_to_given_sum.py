#problem1: Given a list of integer, write a python function to find the two numbers such that they add up to a specific target.
"""
sample input: 2, 7, 11, 15
target = 9
sample output: [0, 1](indices of 2 and 7)
"""
#problem2: Implement a function to perform a binary search on a sorted array and return the index of the target element. if the element is not found, return -1.
"""
sample input: [1, 3, 5, 7, 9, 11, 13]
target = 7
sample output: 3 (index of 7)
"""
# Problem3: Reverse a string in-place
"""
sample input: hello
sample output: olleh
"""

#Problem4: Implement a function to check if a given string is palindrome.
"""
Sample input: a man, a plan, a canal: Panama
Sample output: True
"""

#Problem5: Find the Missing Number: Given a list of numbers from 1 to n, one number is missing. Find that missing number.
"""
sample input: 1 2 3 4 5 6 7 9 10
sample output: 8
"""

#Problem6: Count the words in a string. write a function to count the occurrences of each word in a given string.

#Problem7: Anagrams: check if two strings are anagrams to each other

#Problem8: Find the Maximum Subarray sum: write a function to find the maximum sum of a contiguous subarray within a one-dimensional array of the numbers.

#Problem9: Implement a Queue using Stacks: Implement a queue data structure using two stacks.

#Problem10: Merge Two Sorted Lists: function to merge two sorted linked lists into a single sorted linked list.

#Problem11: Reverse a linked list
#Problem12: 

sinput = [2, 7, 11, 15]

for index in range(len(sinput)):
    for Jerry in range(index):
        print(f"iteration i: {sinput(index)} , Jth value is: {sinput(Jerry)}")

for index, num in enumerate(sinput):

    print(f"index is: {index}, number is: {num}")


print(sinput)

##Problem6: Count the words in a string. write a function to count the occurrences of each word in a given string.

def find_number_of_occurence(string):
    print(string)
    words = {}
    ls = string.split(' ')
    for word in ls:
        words[word] = 0

    for word in ls:
        words[word] = words[word] + 1

    print(words)
    return words

text = input("please enter the text:  ")
text = find_number_of_occurence(text)

# sort the text over key 

['a', 'dog', 'fox', 'jumps', 'lazy', 'log', 'next', 'over', 'sleeping', 'to']
{'a': 3, 'lazy': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'sleeping': 1, 'dog': 1, 'next': 1, 'to': 1, 'log': 1}


