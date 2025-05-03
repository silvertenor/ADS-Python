class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            return None
        return self.stack.pop()

    def peek(self):
        # print(self.stack[-1])
        return self.stack[-1]
    
    def getSize(self):
        return len(self.stack)

    def isEmpty(self):
        return self.stack == []
    
def isBalanced(parenth):
    openStack = Stack()
    for char in parenth:
        if char == '(':
            openStack.push(char)

        elif openStack.pop() is None:
            print('Not valid!')

    print(openStack.isEmpty())
# need to utilize stack to ensure parenthesis are balanced

parenth = '(((()))()())'

isBalanced(parenth)

parenth = '((((()))()())'
isBalanced(parenth)

parenth = '(((()))()())))'
isBalanced(parenth)