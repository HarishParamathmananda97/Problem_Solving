class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertHead(self, newNode):
        tempNode = self.head 
        self.head = newNode
        self.head.next = tempNode
        del tempNode

    def insertat(self, newNode):
        if self.head is None:
            self.head = newNode

        else:
            currentNode = self.head 
            while True:
                if currentNode.next is None:
                    break
                currentNode = currentNode.next 
            currentNode.next = newNode 
    def linkedLength(self):
        length = 0
        currentNode = self.head 
        while currentNode  is not None:
            length += 1
            currentNode = currentNode.next 
        return length
    
    def insertatposition(self, newNode, position):
        if position is 0:
            self.insertHead(newNode)

        if position > self.linkedLength():
            print("Out of range, please enter the position below <", self.linkedLength)
            return

        currentNode = self.head 
        currentPosition = 0

        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode 
                break
            previousNode = currentNode 
            currentNode = currentNode.next 
            currentPosition += 1
    def deleteEnd(self):
        lastNode = self.head 
        while lastNode.next is not None:
            previousNode = lastNode 
            lastNode = lastNode.next 
        previousNode.next = None
    def deleteatposition(self, position):
        currentPosition = 0
        currentNode = self.head 
        while True:
            if currentPosition == position:
                previousNode.next = currentNode.next
                currentNode.next = None
                break
            previousNode = currentNode 
            currentNode = currentNode.next 
            currentPosition += 1 
    def printList(self):
        if self.head is None:
            print("List is empty.")
            return
        currentNode = self.head 
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next 
        
def mergeLists(firstList, secondList, mergedList):
    currentFirst = firstList.head 
    currentSecond = secondList.head 
    while True:
        if currentFirst is None:
            mergedList.insertat(currentSecond)
            break
        if currentSecond is None:
            mergedList.insertat(currentFirst)
            break
        if currentFirst.data < currentSecond.data:
            currentFirstNext = currentFirst.next 
            currentFirst.next = None 
            mergedList.insertat(currentFirst)   
            currentFirst = currentFirstNext 
        else:
            currentSecondNext = currentSecond.next
            currentSecond.next = None
            mergedList.insertat(currentSecond)
            currentSorted = currentSecondNext 




firstNode = Node(1)
linkedList = LinkedList()
# linkedList.insertHead(firstNode)
linkedList.insertat(firstNode)
secondNode = Node(3)
linkedList.insertat(secondNode)
thirdNode = Node(4)
linkedList.insertat(thirdNode)

#second Linked LIst
nodeFour = Node(2)
nodeFive = Node(7)
nodeSix = Node(9)
secondList = LinkedList()
secondList.insertat(nodeFour)
secondList.insertat(nodeFive)
secondList.insertat(nodeSix)

print("Printing first List.")
linkedList.printList()

print("Printing second List.")
secondList.printList()

mergedList = LinkedList()
mergeLists(linkedList, secondList, mergedList)
del linkedList
del secondList 
print("Priting merged list")
mergedList.printList()