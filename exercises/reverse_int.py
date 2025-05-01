def reverse(number):
    number = list(str(number))

    start_index = 0; end_index = len(number) - 1
    while start_index < end_index:
        number[start_index], number[end_index] = number[end_index], number[start_index]
        start_index += 1; end_index -= 1
    
    return int(''.join(number))

def reverse_better(number):
    reversed = 0
    while number > 0:
        


print(reverse(4321))
