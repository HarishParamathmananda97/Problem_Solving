"""
Problem statement
You are given a Singly Linked List of integers and a reference to the node to be deleted. Every node of the Linked List has a unique value written on it. Your task is to delete that node from the linked list.

A singly linked list is a linear data structure in which we can traverse only in one direction i.e. from Head to Tail. It consists of several nodes where each node contains some data and a reference to the next node.

Note:

• The reference to the head of the linked list is not given.
• The node to be deleted is not a tail node.
• The value of each node in the Linked List is unique.
• It is guaranteed that the node to be deleted is present in the linked list.
A sample Linked List-
-5 => 2 => 10 => 15 => Null
 |
Head

Constraints:
1 <= T <= 100
2 <= N <= 5000
-10 ^ 9 <= NODE.DATA <= 10 ^ 9 and node.data != -1

Where 'N' denotes the total number of nodes in the Linked List and 'NODE.DATA' is the value of the node present.

Time limit: 1 sec.

Sample Input 1:
2
2 5 7 10 -1
7
-8 3 4 -2 1 -1
4
Sample Output 1:
2 5 10 -1
-8 3 -2 1 -1

For the first test case, the given Linked List is
2 -> 5 -> 7 -> 10 -> Null
So, after deleting the node 7, the Linked List becomes 2 → 5 → 10 → NULL, which is shown in the below figure.
2->5->7->10->Null
      |
      Deleted
2->5----->10->Null
For the second test case, the given Linked List is
-8->3->4->-2->1->Null
So, after deleting the node 4, the Linked List becomes  -8 → 3 → -2 → 1 → NULL.

Sample Input 2:
2
4 9 10 -1
4
-7 7 -1
-7
Sample Output 2:
9 10 -1
7 -1
Explanation for sample input 2:
For the first test case, the given Linked List is
4 -> 9 -> 10 -> Null
So, after deleting the node 4, the Linked List becomes 9 → 10 → NULL.


For the second test case, the given Linked List is
-7 -> 7 -> Null
So, after deleting the node -7, the Linked List becomes 7 → NULL.

"""

from math import *
from collections import *
from sys import *
from os import *

# Following is the List Node Class
class LinkedListNode:
    def __init__(self, data):

        self.data = data
        self.next = None

    def __del__(self):
        if(self.next):
            del self.next

def deleteNode(node):
    # Write your code here.
    pass