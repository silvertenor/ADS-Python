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
    
    def remove(self, data):
        if self.root:
            self.removeNode(data, self.root)

    def removeNode(self, data, node):
        if not node:
            return
        
        # visit left subtree
        if data < node.data:
            self.removeNode(data, node.leftNode)
        # visit right subtree
        if data > node.data:
            self.removeNode(data, node.rightNode)
        # we have found the node we want to remove:
        else:
            # if no children (leaf node):
            if node.leftNode is None and node.rightNode is None:
                print(f'Removing leaf node: {node.data}')
                parent = node.parent
                if parent is not None and parent.leftNode == node:
                    parent.leftNode = None
                if parent is not None and parent.rightNode == node:
                    parent.rightNode = None
                # remove root node if parent is none
                if parent is None:
                    self.root = None

                # remove node from memory
                del node

            # when there is only a right node
            elif node.leftNode is None and node.rightNode:
                print('Removing a node with single right child...')
                parent = node.parent

                if parent and parent.leftNode == node:
                    parent.leftNode = node.rightNode
                if parent and parent.rightNode == node:
                    parent.rightNode = node.rightNode
                if not parent:
                    self.root = node.rightNode

                # update parent of "downstream" node
                node.rightNode.parent = parent

                # remove node from memory
                del node
            
            # when there is only a left node
            elif node.leftNode and not node.rightNode:
                print('Removing a node with only a left child...')
                parent = node.parent

                if parent and parent.leftNode == node:
                    parent.leftNode = node.leftNode
                if parent and parent.rightNode == node:
                    parent.rightNode = node.rightNode
                if not parent:
                    self.root = node.rightNode
                node.leftNode.parent = parent

                del node

            # remove node with two children
            else:
                # have to find the predecessor (largest item in left subtree):
                predecessor = self.getPredecessor(node.leftNode)
                # swap actual node with predecessor (data only!)
                predecessor.data, node.data = node.data, predecessor.data

                # remove recursively!
                self.removeNode(predecessor.data, predecessor)


    def getPredecessor(self, node):
        if node.rightNode:
            return self.getPredecessor(node.rightNode)
        
        return node




        


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
bst.insert(10)
bst.insert(5)
bst.insert(8)
bst.insert(12)
bst.insert(-5)
bst.traverse()
bst.remove(44) # not present
bst.remove(10)

bst.traverse()