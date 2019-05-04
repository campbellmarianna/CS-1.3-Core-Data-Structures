#!python
# -*- coding: utf-8 -*-

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # Check if list is empty
        if not self.list.head : # empty sequence is False
            return True # list is empty
        return False

    def length(self):
        """Return the number of items in this queue."""
        # Count number of items
        return self.list.length() # Count number of items

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) because we ony change the first
        node and never loop through all nodes."""
        # Insert given item
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # Return front item, if any
        if self.is_empty():
            return None
        else:
            # return item at index
            return self.list.head.data

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) because we ony change the last
        node and never loop through all nodes."""
        # Remove and return front item, if any
        # Raise value error if stack is empty
        if self.is_empty() == True:
            raise ValueError("Queue is empty")
        # Save the item to be deleted
        item = self.front()
        # delete the item from the list
        self.list.delete(self.list.head.data)
        return item


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # Check if empty
        if not self.list: # empty sequence is False
            return True
        return False

    def length(self):
        """Return the number of items in this queue."""
        # Count number of items
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) because we ony change the last
        node and never loop through all nodes due to the tail property."""
        # Insert given item
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # Return front item, if any
        # Check of stack is empty
        if self.is_empty() == True:
            return None
        return self.list[0]

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(n) because we take off the first element
        and move all other elements one position up in the array."""
        # Remove and return front item, if any
        if self.is_empty(): # Constant time to compare values
            # raise error
            raise ValueError('Queue is empty')
        else:
            return self.list.pop(0)
# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
Queue = LinkedQueue
# Queue = ArrayQueue
