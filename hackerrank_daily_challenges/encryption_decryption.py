#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'decryptPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryptPassword(s):
    # Write your code here
    i, n = 0, len(s)
    encrypted_s = ''
    while i < n:
        if i + 1 >= n:
            encrypted_s += s[i]
            return encrypted_s
            
        elif s[i].islower() and s[i+1].isupper():
            encrypted_s += s[i+1] + s[i] + '*'
            i += 2
        elif s[i].isnumeric():
            encrypted_s = s[i] + encrypted_s + '0'
            i += 1
        else:
            encrypted_s += s[i]
            i += 1
            
    return encrypted_s

def decryptPassword(s):
    while '*' in s:
        prefix, suffix = s.split('*',1)
        s = prefix[:len(prefix)-2] + prefix[-1] + prefix[-2] + suffix
        # print(s)
    s = [letter for letter in s]
    s = s[::-1]
    i, n = 0, len(s)
    while i < n:
        if '0' not in s:
            s = s[::-1]
            res = ''.join(s)
            return res
        if s[i] == '0':
            s[i] = s[-1]
            s.pop()
        i += 1
    s = s[::-1]
    return ''.join(s)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    enc_s = encryptPassword(s)
    result = decryptPassword(enc_s)

    fptr.write(result + '\n')

    fptr.close()

##########################################################################
""" ChatGPT optimized the above code better, lets learn that as well."""
def encryptPassword(s):
    i, n = 0, len(s)
    encrypted_s = []
    while i < n:
        if i + 1 < n and s[i].islower() and s[i + 1].isupper():
            encrypted_s.append(s[i + 1])
            encrypted_s.append(s[i])
            encrypted_s.append('*')
            i += 2
        elif s[i].isdigit():
            encrypted_s.insert(0, s[i])
            encrypted_s.append('0')
            i += 1
        else:
            encrypted_s.append(s[i])
            i += 1

    return ''.join(encrypted_s)

def decryptPassword(s):
    # Handle the '*'
    parts = s.split('*')
    reconstructed = []
    for part in parts:
        if len(part) > 1 and part[-2].islower() and part[-1].isupper():
            reconstructed.append(part[:-2])
            reconstructed.append(part[-1])
            reconstructed.append(part[-2])
        else:
            reconstructed.append(part)
    s = ''.join(reconstructed)
    
    # Handle the digits and '0's
    digit_stack = []
    result = []
    for char in s:
        if char == '0':
            result.append(digit_stack.pop())
        elif char.isdigit():
            digit_stack.append(char)
        else:
            result.append(char)

    return ''.join(result)

if __name__ == '__main__':
    s = input()  # e.g., 'aP1pL5e'

    enc_s = encryptPassword(s)  # e.g., '51Pa*0Lp*0e'
    print(f'Encrypted: {enc_s}')

    result = decryptPassword(enc_s)  # e.g., 'aP1pL5e'
    print(f'Decrypted: {result}')
