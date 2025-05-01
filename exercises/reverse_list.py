def reverse(nums):

    # pointing to the first item
    start_index = 0
    end_index = len(nums)-1
    while end_index > start_index:
        # keep swapping items
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index += 1
        end_index -= 1
    
    return nums

if __name__ == '__main__':
    n = [1, 2, 3, 4]
    reverse(n)
    print(n)
