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

        if guess == item: #
            return mid
        elif guess > item: # the guess was to high
            high = mid - 1
        else: # the guess was to low
            low = mid + 1

    return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))  # Expected output: 1 (correct index of 3)