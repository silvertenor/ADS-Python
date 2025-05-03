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
    


# Need to convert decimal numbers to binary numbers!


def convertToBinary(num):
    if num < 0:
        return
    numStack = Stack()
    while num > 0:
        remainder = num % 2 
        numStack.push(remainder)
        num = num // 2

    binary = ''
    while not numStack.isEmpty():
        binary += str(numStack.pop())
    return binary


num = 10
print(convertToBinary(num))

num = 135
print(convertToBinary(num))