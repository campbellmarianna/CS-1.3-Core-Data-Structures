#!python
from linkedlist import LinkedList

class LinkedSet(object):

    def __init__(self, iterable=None):
        """Initialize this set and add the given elements, if any."""
        self.list = LinkedList()
        if iterable is not None:
            for element
