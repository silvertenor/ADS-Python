from ll import Node


class OrderedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def size(self):
        return self.size
    
    def add(self, data):
        if not self.head:
            node = Node(data)
            self.head = node
            return
        
        node = Node(data)
        current = self.head
        pvs = None
        while current and current.data < data:
            pvs = current
            current = current.next

        next = current
        if pvs:
            pvs.next = node
        else:
            self.head = node
        node.next = next

    def search(self, data):
        if not self.head:
            return None
        
        current = self.head

        while current:
            if current.getData() == data:
                return True
            if current.getData() > data:
                return False
            current = current.next
        
        return False


    def traverse(self):
        if not self.head:
            return
        
        current = self.head
        # print(self.head.getData())
        while current:
            print(current.getData())
            current = current.getNext()

ol = OrderedList()
ol.add(15)
ol.add(32)
ol.add(19)
ol.add(13)
ol.add(35)

print(ol.traverse())