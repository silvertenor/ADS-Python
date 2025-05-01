# doubly linked lists not only have reference to head node, but also to the tail node
# every single node has reference to next node and previous node
# pvs node of head and next node of tail are both null
# data, pvs node, and next node are contents
# advantages - 
    # head & tail nodes can be accessed in O(1) running time
    # can be traversed in both directions
    # removing a node is easier because there is pointer to previous node as well
# disadvantages -
    # need more memory (2 pointers)
    # more complicated to implement


class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.pvsNode = None

    def __repr__(self):
        return str(self.data)
    
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    # this operation inserts items at end of LL
    # we have to manipulate tail node in O(1)
    def insert(self, data):
        newNode = Node(data)
        self.len += 1
        # if LL is empty
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        # if LL has at least 1 item
        else:
            self.tail.nextNode = newNode
            newNode.pvsNode = self.tail
            self.tail = newNode
    
    def traverseForward(self):
        if self.head is None:
            return
        actualNode = self.head
        while actualNode is not None:
            print(actualNode)
            actualNode = actualNode.nextNode
    
    def traverseBack(self):
        if self.tail is None:
            return
        actualNode = self.tail
        while actualNode is not None:
            print(actualNode)
            actualNode = actualNode.pvsNode


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert('test')
    ll.insert('test2')
    ll.traverseForward()
    ll.traverseBack()