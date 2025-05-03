class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.leftNode = None
        self.rightNode = None
        # Crucial when implementing remove function
        self.parent = parent




class BinarySearchTree:

    def __init__(self):
        # We can access root node exclusively
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data) # no parent
        else:
            self.insertNode(data, self.root)
            # actualNode = self.root
            # while actualNode is not None:
            #     if data < actualNode.data:
            #         if actualNode.leftNode is None:
            #             actualNode.leftNode = Node(data, parent=actualNode)
            #             break
            #         actualNode = actualNode.leftNode
            #     elif data > actualNode.data:
            #         if actualNode.rightNode is None:
            #             actualNode.rightNode = Node(data, parent=actualNode)
            #             break
            #         actualNode = actualNode.rightNode
            #     else:
            #         print("invalid entry!")
            #         return None

    def insertNode(self, data, node):

        if data < node.data:
            if node.leftNode:
                self.insertNode(data, node.leftNode)
            else:
                node.leftNode = Node(data, parent=node)
        elif data > node.data:
            if node.rightNode:
                self.insertNode(data, node.rightNode)
            else:
                node.rightNode = Node(data, parent=node)
        else:
            print("invalid entry!")

    def getMin(self):
        if self.root is None:
            print("Empty BST!")
            return
        else:
            return self.getMinValue(self.root)

    def getMinValue(self, node):
        if node.leftNode:
            return self.getMinValue(node.leftNode)
        
        return node.data
    
    def getMax(self):
        if self.root is None:
            print("Empty BST!")
            return
        
        else:
            return self.getMaxValue(self.root)
        
    def getMaxValue(self, node):
        if node.rightNode:
            return self.getMaxValue(node.rightNode)
        
        return node.data
    
    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    # O(N) linear runtime complexity
    def traverseInOrder(self, node):
        if node.leftNode:
            self.traverseInOrder(node.leftNode)
        print(node.data)
        if node.rightNode:
            self.traverseInOrder(node.rightNode)

    def traverseReverse(self):
        if self.root:
            self.traverseInReverseOrder(self.root)
    def traverseInReverseOrder(self, node):
        if node.rightNode:
            self.traverseInReverseOrder(node.rightNode)
        print(node.data)
        if node.leftNode:
            self.traverseInReverseOrder(node.leftNode)
        

        


bst = BinarySearchTree()
bst.insert(15)
bst.insert(35)
bst.insert(40)
bst.insert(10)
bst.insert(12)
# print(bst.getMin())
# print(bst.getMax())
# bst.traverse()
bst.traverseReverse()