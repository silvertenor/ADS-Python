import time
import random
import numpy as np
# LIFO structure
class Stack:

    def __init__(self):
        self.stack = [] # 1-D array as structure to implement stack behavior

    # O(N) runtime - has to look through every item of array
    def getMax(self):
        if self.stack == []:
            return None
        return max(self.stack)

    # insert item into stack
    def push(self, data):
        self.stack.append(data)
    
    # remove item from stack and return last item we have inserted (LIFO)
    def pop(self):
        if self.stackSize() < 1:
            return
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    # peek: returns last item without removing it

    def peek(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return self.stack == [] # boolean
    
    def stackSize(self):
        return len(self.stack)
    

class StackWithMax:

    def __init__(self):
        self.stack = [] # 1-D array as structure to implement stack behavior
        self.maxStack = [] # 1-D array of maximum of stack (only appended to if new data greater than previous data)

    # insert item into stack
    def push(self, data):
        if self.stack == []:
            self.maxStack.append(data) # first entry is always max
        # check if new data bigger than (or equal to) existing max
        else:
            # using if equal to in case there are duplicate entries in original stack u
            if data >= self.maxStack[-1]:
                self.maxStack.append(data)
        
        # append to regular stack regardless
        self.stack.append(data)
    
    # O(1) constant runtime - always looks at last value of array
    def getMax(self):
        if self.stack == []:
            return None
        return self.maxStack[-1]
    
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
    


def runtime_measurement(stack, arr):
    # size = 100000
    # random.seed(0)
    # arr = [random.randint(-100000, 100000) for _ in range(size)]
    

    now = time.time()

    print("pushing...")
    for item in arr:
        stack.push(item)
        maxNum = stack.getMax()
        if item == maxNum:
            print(f'Max of Stack: {maxNum}')
    print("popping...")
    for item in arr[::-1]:
        stack.pop()
        if item == maxNum:
            print(f'Max of Stack: {maxNum}')
        maxNum = stack.getMax()

    end = time.time()
    print(f'Code ran in {end-now} seconds')

arr = np.random.choice(2500, 40000, replace=True)
stack = StackWithMax()
runtime_measurement(stack, arr)
stack = Stack()
runtime_measurement(stack, arr)