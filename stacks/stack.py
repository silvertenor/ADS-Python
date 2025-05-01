# LIFO structure

class Stack:

    def __init__(self):
        self.stack = [] # 1-D array as structure to implement stack behavior

    # insert item into stack
    def push(self, data):
        self.stack.append(data)
    
    # remove item from stack and return last item we have inserted (LIFO)
    def pop(self):
        if self.stackSize() < 1:
            return
        data = self.stack[-1]
        self.stack.remove(data)
        return data
    
    # peek: returns last item without removing it

    def peek(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return self.stack == [] # boolean
    
    def stackSize(self):
        return len(self.stack)
    


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f'Size: {stack.stackSize()}')
print(f'Popped item: {stack.pop()}')
print(f'Size: {stack.stackSize()}')
print(f'Peek item: {stack.peek()}')
print(f'Size: {stack.stackSize()}')
print(f'Popped item: {stack.pop()}')
print(f'Popped item: {stack.pop()}')
print(f'Popped item: {stack.pop()}')
print(f'Popped item: {stack.pop()}')