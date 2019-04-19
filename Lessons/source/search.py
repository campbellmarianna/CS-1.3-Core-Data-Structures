#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # implement linear search recursively here
    # Check for index-range error
    if index >= len(array): # base case 1
        return None
    # If we find the item, stop recursing and return the index
    elif item == array[index]: # base case 2
        return index

    # Item not yet found, try the next index
    else:
        print("array: {}, item: {}, index: {}".format(array, item, index))
        return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # found = False
    left = 0
    right = len(array) - 1

    while left <= right:
        midpoint = (left + right) // 2

        if item == array[midpoint]:
            return midpoint
        elif array[midpoint] < item:
            left = midpoint + 1
        else:
            right = midpoint - 1

    return None # Never found item



def binary_search_recursive(array, item, left=None, right=None):
    # give left and right values for first iteration
    if left is None and right is None: # make sure that both or neither valuse is set
        left = 0
        right = len(array) - 1
    elif left is None or right is None: # one of these values wasn't set
        raise AssertionError("Please provide both left AND right or neither")

    midpoint = (left + right) // 2


    if left > right: # base case 1
        return None

    if array[midpoint] == item: #base case 2
        print(midpoint)
        return midpoint

    # if the item is larger than midpoint value, search right of midpoint
    if array[midpoint] < item:
        left = midpoint + 1
        return binary_search_recursive(array, item, left, right)

    # item must be smaller than midpoint value, search left of midpoint
    right = midpoint - 1
    return binary_search_recursive(array, item, left, right)

if __name__ == '__main__':
    # print(linear_search([3, 4, 2, 1, 7], 8))
    print(binary_search([1,3,4,5,6], 6))
