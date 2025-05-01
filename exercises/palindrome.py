def is_palindrome(word):

    if word == word[::-1]:
        return True
    
    return False

def is_palindrome_harder(word):
    original_string = word
    reversed_string = reverse(original_string)

    if original_string == reversed_string:
        return True
    
    return False

def reverse(word):
    # convert string into list of characters
    word = list(word)
    # pointing to the first item
    start_index = 0
    end_index = len(word)-1
    while end_index > start_index:
        # keep swapping items
        word[start_index], word[end_index] = word[end_index], word[start_index]
        start_index += 1
        end_index -= 1
    
    return ''.join(word)
word = "racecar"
print(is_palindrome(word))

word = 'doghead'
print(is_palindrome(word))

word = "racecar"
print(is_palindrome_harder(word))

word = 'doghead'
print(is_palindrome_harder(word))