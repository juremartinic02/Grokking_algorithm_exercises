def binary_search(array, item):
    """
    We have to keep track of what part of array are we searching.
    At the beginning we are searching the entire array to find the target element.
    """
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None  # Fixed: Moved outside the loop

my_list = [1, 3, 5, 7, 9]  # Renamed to avoid shadowing 'list'
print(binary_search(my_list, 3))  # Output: 1 (correct index of 3)