class Queue:

    def __init__(self):
        '''Create new queue'''
        self._items = []

    def isEmpty(self):
        '''Check if queue is empty'''
        return self._items == []

    def enqueue(self, data):
        '''Add item to "end" of queue'''
        self._items.insert(0, data)

    def dequeue(self):
        '''Remove item from "start" of queue'''
        return self._items.pop()

    def size(self):
        '''Get size of queue'''
        return len(self._items)


q = Queue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
print(q.isEmpty())
q.enqueue(8.4)
q.dequeue()
q.dequeue()
print(q.size())