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


s = Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.getSize())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.getSize())