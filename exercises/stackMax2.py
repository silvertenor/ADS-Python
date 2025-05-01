class StackWithMax:

    def __init__(self):
        self.stack = [] # 1-D array as structure to implement stack behavior
        self.maxStack = [] # 1-D array of maximum of stack (only appended to if new data greater than previous data)

    # insert item into stack
    def push(self, data):
        self.stack.append(data)
        if len(self.stack) == 1:
            self.maxStack.append(data) # first entry is always max
        # check if new data bigger than (or equal to) existing max
        else:
            # using if equal to in case there are duplicate entries in original stack
            if data >= self.maxStack[-1]:
                self.maxStack.append(data)

        
    
    def getMax(self):
        if self.stack == []:
            return None
        return self.maxStack[-1] # largest always at "end"
    # remove item from stack and return last item we have inserted (LIFO)
    def pop(self):
        if self.stackSize() < 1:
            return
        data = self.stack[-1]
        del self.stack[-1]
        # check if data being removed is equal to max of stack
        if data == self.maxStack[-1]:
            del self.maxStack[-1]
        return data
    
    # peek: returns last item without removing it
    def peek(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return self.stack == [] # boolean
    
    def stackSize(self):
        return len(self.stack)
    

stack = StackWithMax()
stack.push(10)
print(f'Max of stack: {stack.getMax()}')
stack.push(20)
print(f'Max of stack: {stack.getMax()}')
stack.push(10)
print(f'Max of stack: {stack.getMax()}')
stack.push(20)
print(f'Max of stack: {stack.getMax()}')
stack.push(40)
print(stack.stack)
print(stack.maxStack)
print(f'Max of stack: {stack.getMax()}')
print(f'Deleted data: {stack.pop()}')
print(f'Max of stack: {stack.getMax()}')
print(f'Deleted data: {stack.pop()}')
print(f'Max of stack: {stack.getMax()}')
print(f'Deleted data: {stack.pop()}')
print(f'Max of stack: {stack.getMax()}')
print(f'Deleted data: {stack.pop()}')
print(f'Max of stack: {stack.getMax()}')