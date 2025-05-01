class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    # O(N) linear running time complexity
    def reverse(self):
        currentNode = self.head
        pvsNode = None
        nextNode = None
        while currentNode is not None:
            nextNode = currentNode.next_node
            currentNode.next_node = pvsNode
            pvsNode = currentNode
            currentNode = nextNode
        self.head = pvsNode
        
            
        

    def insert(self, data):

        self.size = self.size + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
            
    def get_head(self):
        return self.head

    def traverse_list(self):

        actual_node = self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next_node

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    print(ll.traverse_list())
    ll.reverse()
    print(ll.traverse_list())