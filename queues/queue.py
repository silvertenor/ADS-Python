# FIFO

class Queue:

    def __init__(self):
        self.queue = [] # store items in 1-D array (implementation of abstract data type queue)

    # O(1) runtmime
    def isEmpty(self):
        return self.queue == []
    
    def enqueue(self, data):
        self.queue.append(data)
    
    # O(N) runtime
    def dequeue(self):
        data = self.queue[0]
        self.queue.remove(data)
        return data
    
    # O(1) runtime
    def peek(self):
        return self.queue[0]
    
    # O(1) runtime
    def sizeOf(self):
        return len(self.queue)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(f'Size of Queue: {queue.sizeOf()}')
print(f'Dequeue: {queue.dequeue()}')
print(f'Size of Queue: {queue.sizeOf()}')