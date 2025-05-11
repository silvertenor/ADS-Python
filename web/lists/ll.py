class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def getData(self):
        return self._data
    
    def setData(self, data):
        self._data = data

    data = property(getData, setData)

    def getNext(self):
        return self._next
    
    def setNext(self, nextNode):
        self._next = nextNode

    next = property(getNext, setNext)

    def __str__(self):
        return str(self.getData())
    

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None
    
    def size(self):
        if self.head is None:
            return 0
        
        size = 0
        actualNode = self.head
        while actualNode is not None:
            actualNode = actualNode.getNext()
            size += 1
        return size
    
    def add(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.setData(data)
        else:
            node = Node(data)
            node.setData(data)
            actualNode = self.head
            while actualNode.next is not None:
                actualNode = actualNode.getNext()

            actualNode.setNext(node)
    def remove(self, data):
        if not self.head:
            return
        

        if self.head.getData() == data:
            temp = self.head
            del self.head
            self.head = temp.getNext()
            return
            
        current = self.head
        previous = None
        if self.search(data):
            while current.getData() != data:
                previous = current
                current = current.getNext()
            previous.setNext(current.getNext())
            del current

    def traverse(self):
        if not self.head:
            return
        
        current = self.head
        # print(self.head.getData())
        while current:
            print(current.getData())
            current = current.getNext()

    def search(self, data):
        if not self.head:
            return None
        
        actual = self.head
        while actual is not None and actual.getData() != data:
            actual = actual.getNext()

        if actual:
            return actual
        return None

    
ll = UnorderedList()
ll.add(31)
ll.add(77)
ll.add(17)
ll.add(93)
ll.add(26)
ll.add(54)

# print(ll.search(93))
# print(ll.search(91))

ll.remove(31)
ll.remove(17)
ll.remove(93)
ll.remove(54)
# ll.traverse()

