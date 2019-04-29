#!python
from hashtable import HashTable

class Set(object):

    def __init__(self, elements=None):
        """Initialize this set and add the given elements, if any."""
        self.ht = HashTable()
        self.size = 0 # Number of elements
        if elements is not None:
            for element in elements:
                self.add(element)

    def contains(element):
        pass

    def add(element):
        pass

    def remove(element):
        pass

    def union(other_set):
        pass

    def intersection(other_set):
        pass

    def difference(other_set):
        pass

    def is_subset(other_set):
        pass
