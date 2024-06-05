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
        
    
firstNode = Node(10)
linkedList = LinkedList()
linkedList.insertHead(firstNode)
secondNode = Node(15)
linkedList.insertat(secondNode)
thirdNode = Node(5)
linkedList.insertatposition(thirdNode, 2)
linkedList.printList()
linkedList.deleteEnd()
linkedList.printList()
thirdNode = Node(5)
linkedList.insertat(thirdNode)
print("going to delete the position at 1 next.")
linkedList.deleteatposition(1)
linkedList.printList()

