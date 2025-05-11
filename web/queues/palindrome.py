from dequeue import Dequeue


def isPalindrome(word):
    d = Dequeue()
    for char in word:
        d.addFront(char)
    
    while d.size() > 1:
        front = d.removeFront()
        rear = d.removeRear()
        if front != rear:
            return False
        
    return True

word = input("Please enter a word to see if it is a palindrome: ")
print(isPalindrome(word))


