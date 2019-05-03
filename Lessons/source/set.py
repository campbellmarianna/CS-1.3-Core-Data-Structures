#!python
from hashtable import HashTable

class Set(object):

    def __init__(self, elements=None):
        """Initialize this set and add the given elements, if any."""
        self.ht = HashTable()
        self.size = 0 # Number of elements
        if elements is not None:
            for element in elements:
                # print('Element:', element)
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
        """Remove element from this set, if present, or else raise KeyError
        Running Time: O(l)"""
        if self.contains(element):
            self.ht.delete(element)
            self.size -= 1 # Update size
        else:
            raise KeyError('Element not found: {}'.format(element))

    def union(self, other_set):
        """Return a new set that is the union of this set and other_set
        Running Time: O(n) for looping through each entry in the sets to find
        where they match"""
        # get items of both set and other_set
        # Initialize new_set
        new_set = Set()
        set = self.ht.items()
        other_set = other_set.ht.items()
        # loop through elements and both sets
        for set_entry in set:
            for other_set_entry in other_set:
                # check if the contains is true
                if self.contains(set_entry) and other_set.contains(other_set_entry):
                    new_set.add(set_entry)
                #     then append then to new_set
        # if not continue till done
        return new_set

    def intersection(self, other_set):
        """Return a new set that is the interection of this set and other_set
        Running Time: O(n) for looping through each entry in the sets to find
        where they match"""
        # Initialize new_set
        new_set = Set()
        set = self.ht.items()
        other_set = other_set.ht.items()
        for set_entry in set:
            for other_set_entry in other_set:
                # check if a element in this set is the same in the other_set
                if set_entry[1] == other_set_entry[1]:
                    # append to new_set
                    new_set.add(set_entry)
                else:
                    continue
        return new_set

    def difference(self, other_set):
        """Return a new set that is the difference of this set and other_set
        Running Time: O(n) for looping through each key in the set to check
        if a key in the set is in the other set """
        # Initialize new_set                                                      # Inspired by Dylan Finn
        new_set = Set()
        # loop through the keys of the set
        for set_key in self.ht.keys():
            # if not in other set
            if not other_set.ht.contains(set_key):
                # add key to new set
                new_set.add(set_key)
        return new_set

    def is_subset(self, other_set):
        """Return a boolean indicating whether other_set is a subset of this set
        Running Time: O(n) for looping through each key in the set to check if
        each one is in the subset"""
        # create a counter found
        found = 0
        # loop through the keys of the other set and check if they are in this set
        for other_set_key in other_set.ht.keys():
            if self.ht.contains(other_set_key):
                # if so then w increment found
                found += 1
        # check if all entries were found in sub_set
        if found == other_set.ht.length():
            return True
        return False

if __name__ == '__main__':
    s = Set([4, 5, 9, 8])
    assert s.size == 4
    other_set = Set([5, 9])
    print(s.is_subset(other_set))
