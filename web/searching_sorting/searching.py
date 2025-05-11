# Sequential search:
# start at first item of the list, and move from item to item until either found or end of list is reached


# This is not very efficient, and can be as bad as O(N) time (in an unordered list)
# If it's ordered, you can stop as soon as you find the item (or find it is less than the current number if not found)
def seqSearch(arr, item):

    pos = 0

    while pos < len(arr):
        if arr[pos] == item:
            return True
        pos += 1

    return False

arr = [1, 2, 32, 8, 17, 19, 13]
print(seqSearch(arr, 3))
print(seqSearch(arr, 13))
print('-' * 80)

# Binary Search

# If we can get rid of half the items each iteration, we can run logn time
def binarySearch(arr, item):
    low = 0; high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < item:
            low = mid + 1
        elif arr[mid] > item:
            high = mid - 1

        else:
            return mid

arr = [1, 2, 3, 4, 5]
print(binarySearch(arr, 2))
print(binarySearch(arr, 4))