class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            return
        return self.stack.pop()

    def peek(self):
        # print(self.stack[-1])
        return self.stack[-1]
    
    def getSize(self):
        return len(self.stack)

    def isEmpty(self):
        return self.stack == []
    
def reverseString(myString):
    stackString = Stack()
    for char in myString:
        stackString.push(char)
    reversed = ''
    while not stackString.isEmpty():
        reversed += stackString.pop()

    return reversed


stringer = 'dog'
print(reverseString(stringer))