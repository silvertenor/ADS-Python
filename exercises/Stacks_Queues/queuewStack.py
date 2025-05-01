class Queue:

    def __init__(self):
        self.enqueueStack = []
        self.dequeueStack = []

    def enqueue(self, data):
        self.enqueueStack.append(data)
        

    def dequeue(self):
        if len(self.enqueueStack) == 0 and len(self.dequeueStack) == 0:
            raise Exception("Stacks are empty!")
        
        # if stack is empty have to add items O(N) time
        if len(self.dequeueStack) == 0:
            # iterate through enqueueStack to pop all items and push them in reverse order to dequeue stack:
            while len(self.enqueueStack) != 0:
                self.dequeueStack.append(self.enqueueStack.pop())
        
        return self.dequeueStack.pop()
    

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue.dequeue())
    queue.enqueue(40)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())