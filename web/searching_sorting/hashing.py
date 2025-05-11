# Knowing that a list was ordered, we can use binary search
# We can go one step further: build a DS that can be searched in O(1) time

# We need to know even more about where items might be when we go to look for them in the collection
# If every item is where it should be, then the search can use a single comparison

# Hash table - collection of items that makes it easy to find them later.
# Each position (slot) of hash table can hold an item and is named by an integer value starting at 0
# Initially, hash table contains no items so every slot is empty
# Can implement one by using a list w/ each element initialized to None
# 0     1       2       3       4       5       6       ...
# None  None    None    None    None    None    None    ...

# Mapping between an item and the slot where it belongs in the hash table is called "hash function"
# Hash function will take any item in the collection and return an int in the range of slot names b/w 0 and m-1


# Example - remainder method:
# Items 54, 26, 93, 17, 77, and 31 need to be stored (but remember hash table size is 11 for this example)
# Hash mapping takes an item and divides it by the table size, returning the remainder as its hash value
# h(item) = item % 11
# Hash table:

# Item                  Hash Value
# 54                    10
# 26                    4
# 93                    5
# 17                    6
# 77                    0
# 31                    9

# Once hash values have been computed, can insert each item into the hash table at the designated position

# 0     1       2       3       4       5       6       7       8       9       10
# 77    None    None    None    26      93      17      None    None    31      54
# 
# Now when we search for an item, we simply use the hash function to compute the slot name then check hash table to see if it's present
# O(1)!
# This only works if there are no collisions!
# 
# 

'''HASH FUNCTIONS'''
'''
Given a collection of items, a hash function that maps each item into unique slot is referred to as a perfect hash function.
Goal is to create a hash function that minimizes number of collisions, easy to compute, and evenly distributes items in table

Example - folding method:
Begins by dividing item into equal-sized pieces (last piece may not be of equal size)
pieces are then added together to give resulting hash value
ex: phone number - 436-555-4601: take digits and divide them into groups of 2:
(43, 65, 55, 46, 01).
After addition, (43 + 65 + 55 + 46 + 01) % 11 , we get 1 : the phone number would be stored in slot 1

'''


# We can also create hash functions for char-based items such as strings.
# Ex: word "cat" can be thought of sequence of ordinal values:
print(ord('c'))
print(ord('a'))
print(ord('t'))

# We can then take these three ordinal values, add them, and use the remainder method to get a hash value:
def hash_str(string, tableSize):
    return sum([ord(c) for c in string]) % tableSize
print(hash_str('cat', 11))


# If collision happens, need to resolve. One method is linear probing
# Linear probing: sequentially moving through slots (starting with original hash value pos) until we find one that is empty
# Sometimes requires circling back to the first slot to cover the entire table.



# Maps: 