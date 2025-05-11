# DOUBLE-ENDED QUEUE
# Ordered collection of items similar to queue
# Has two ends, front and rear
# Different is unrestrictive nature of adding and removing items
# New items can be added at front or rear; existing items can be removed from either end
# Provides all capabilites of stacks and queues in single data structure

# Does not require LIFO and FIFO orderings that are enforced by stacks and queues
# Up to us to make consistent use of the addition and removal operations


class Dequeue:

    def __init__(self):
        self._items = []

    def isEmpty(self):
        return self._items == []
    
    def addFront(self, data):
        self._items.insert(0, data)

    def addRear(self, data):
        self._items.append(data)

    def removeFront(self):
        return self._items.pop(0)

    def removeRear(self):
        return self._items.pop()

    def size(self):
        return len(self._items)
    

# d = Dequeue()
# print(d.isEmpty())
# d.addRear(4)
# d.addRear('dog')
# d.addFront('cat')
# d.addFront(True)
# print(d.size())
# print(d.isEmpty())
# d.addRear(8.4)
# print(d.removeRear())
# print(d.removeFront())