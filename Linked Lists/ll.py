

class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def __repr__(self):
        return str(self.data)


class LinkedList:

    def __init__(self):
        # first node of linked list
        # We can access this node exclusively - others are by following pointers!
        self.head = None
        self.numNodes = 0

    def sizeOfList(self):
        return self.numNodes
    
    # O(1) constant running time
    def insertStart(self, data):
        self.numNodes += 1
        newNode = Node(data)
        # if first item inserted:
        if self.head is None:
            self.head = newNode
        # if linked list not empty:
        else:
            # Update the references
            newNode.nextNode = self.head
            self.head = newNode
    def insertEnd(self, data):
        self.numNodes += 1
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        # when linked list is not empty
        else:
            actualNode = self.head
            while actualNode.nextNode is not None:
                actualNode = actualNode.nextNode

            actualNode.nextNode = newNode
    
    def remove(self, data):
        self.numNodes -= 1
        # list is empty
        if self.head is None:
            return 
        
        actualNode = self.head
        pvsNode = None
        while actualNode.data != data and actualNode.nextNode is not None:
            pvsNode = actualNode
            actualNode = actualNode.nextNode
        
        # if last element in list
        if actualNode.nextNode is None:
            pvsNode.nextNode = None
        else:
            actualNode.data = actualNode.nextNode.data
            actualNode.nextNode = actualNode.nextNode.nextNode
            
        

        


    # O(N) linear running time complexity
    def traverse(self):
        actualNode = self.head
        while actualNode is not None:
            print(actualNode)
            actualNode = actualNode.nextNode

if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.insertStart(10)
    linkedList.insertStart('Adam')
    linkedList.insertStart(7.5)
    linkedList.insertEnd(100)
    linkedList.insertEnd(1000)
    linkedList.traverse()

    linkedList.remove(1000)
    linkedList.traverse()

