#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests


    # return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    pass
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # found = False
    left = 0
    right = len(array) - 1

    while left <= right:
        midpoint = (left + right) // 2
        print("midpoint: ", midpoint)
        # if len(array) == 1
        if item == array[midpoint]:
            print("array {}, item {}, midpoint {}".format(array, item, midpoint))
            return midpoint
        elif array[midpoint] < item:
            print("array {}, item {}, midpoint {}".format(array, item, midpoint))
            print("I'm HERE")
            left = midpoint + 1
        else:
            print("array {}, item {}, midpoint {}".format(array, item, midpoint))
            print("The item is lower")
            right = midpoint - 1

    return None


    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

if __name__ == '__main__':
    print(binary_search([1,3,4,5,6], 6))
