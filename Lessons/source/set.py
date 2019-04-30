#!python
from hashtable import HashTable

class Set(object):

    def __init__(self, elements=None):
        """Initialize this set and add the given elements, if any."""
        self.ht = HashTable()
        self.size = 0 # Number of elements
        if elements is not None:
            for element in elements:
                print('Element:', element)
                self.add(element)

    def contains(self, element):
        """ Return a boolean indicating whther element is in this set
        Running time: 0(1) """
        #  find bucket index traverse nodes until you find it            # Inpsired by Faith Chikwekwe
        return self.ht.contains(element)

    def add(self, element):
        """ Add element to this set, if not present already
        Running time: 0(l)"""
        if not self.contains(element): # element found
            self.ht.set(element, element)
            self.size += 1 # Update size


    def remove(self, element):
        """Remove element from this set, if present, or else raise KeyError"""
        pass

    def union(self, other_set):
        pass

    def intersection(self, other_set):
        pass

    def difference(self, other_set):
        pass

    def is_subset(other_set):
        pass

if __name__ == '__main__':
    s = Set([1, 2, 3])
    print(s.size)
    print(s.contains(2))
