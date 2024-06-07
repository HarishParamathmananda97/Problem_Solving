from os import *
from sys import *
from collections import *
from math import *

def fishEater(fishes):
    # Write your code here.
    pass

# Main.
t = int(input())
for i in range(t):
    n = int(input())
    fishes = list(map(int,input().split()))
    print(fishEater(fishes))
    