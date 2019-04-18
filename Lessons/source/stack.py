#!python
# -*- coding: utf-8 -*-
from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # Check if empty
        if self.list.head is None:
            return True
        return False

    def length(self):
        """Return the number of items in this stack."""
        return self.list.length() # Count number of items

    def push(self, item):
        """Insert the given item on the top of this stack.
        Best and worst case running time: O(1) because we add one node to the top of the
        the stack and never loop through all nodes."""
        # Push given item
        # Append item to list
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # Return top item, if any
        # Check if stack is empty
        if self.is_empty() == True:
            return None
        else:
            # return item at index
            return self.list.head.data



    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) because we ony delete the head or the first and don't
        have to traverse the rest of the list."""
        # Remove and return top item, if any
        # Raise value error if stack is empty
        if is_empty() == True:
            raise ValueError("Stack is empty")
        # Save the item to be deleted
        item = self.peek()
        # delete the item from the list
        self.list.delete(item)
        # return the item deleted
        return item


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # Check if empty
        if not self.list:
            return True
        else: # If first is not empty
            return False

    def length(self):
        """Return the number of items in this stack."""
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) because we ony change the first
        element and never loop through all elements."""
        # Insert given item
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # Return top item, if any
        # Check of stack is empty
        if self.is_empty() == True:
            return None
        return self.list[-1]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) because we ony change the pop the last element
        and never loop through all elements."""
        # Remove and return top item, if any
        # Check of stack is empty
        if self.is_empty(): # Constant time to compare values
            # raise error
            raise ValueError('Stack is empty')
        else:
            return self.list.pop() # Constant time to pop an element from a list
            # https://wiki.python.org/moin/TimeComplexity


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack
