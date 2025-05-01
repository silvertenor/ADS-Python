#  abstract data type - can be implemented with either array or linked list
# FIFO structure - first item inserted is first item taken out
# basic operations are inserting into queue (enqueue()) and removing (dequeue()) along with peek() - returns value without removing first item
# several applications in operating systems etc.
# useful when resource is shared w/ serveral consumers - i.e. threads
# threads are stored in queues
# queues important in CPU scheduling
# when data transferred async between two processes
# graph algorithms rely heavily on queues: breadth-first search use queues as abstract data type