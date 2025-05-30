# One of most useful Python collections is the dictionary
# key-data pairs
# Key used to look up associated data. Often refer to this idea as a map

# Map abstract data type is an unordered collection of associations between key and data value
# Keys in map are all unique!




class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size # holds keys
        self.data = [None] * self.size # holds data

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        # Collision
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data # replace
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while (
                    self.slots[next_slot]
                    and self.slots[next_slot] != key
                ):
                    next_slot = self.rehash(next_slot, len(self.slots))

                if not self.slots[next_slot]:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data

                else:
                    self.data[next_slot] = data

    def hash_function(self, key, size):
        return key % size
    

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size
    
    def get(self, key):
        startSlot = self.hash_function(key, len(self.slots))

        position = startSlot
        while self.slots[position]:
            if self.slots[position] == key:
                return self.data[position]
            
            else:
                position = self.rehash(position, len(self.slots))
                if position == startSlot:
                    return None
                
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        self.put(key, data)


h = HashTable()
h[54] = 'cat'
h[26] = 'dog'
h[93] = 'lion'
print(h.slots)