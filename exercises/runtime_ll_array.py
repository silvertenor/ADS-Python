import time

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
    def insert(self, data):
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


if __name__ == '__main__':
    ll = LinkedList()
    now = time.time()

    for i in range(500000):
        ll.insert(i)
    
    print(f'Inserting items into linked list in {time.time()-now}s')

    arr = []
    now = time.time()

    for i in range(500000):
        arr.insert(0, i)

    print(f'Inserting items into array in {time.time()-now}s')