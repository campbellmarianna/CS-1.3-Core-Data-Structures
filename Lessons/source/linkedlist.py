#!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

# Prior thought process: 0(n) no matter what you have to loop
# through each bucket in the LinkedList.
    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Best and worst case running time: 0(n) for n nodes in the list because
        we have to iterate over all n nodes and count 1 for each"""
        # Node counter initialized to zero
        node_count = 0 # Constant time to assign a variable to an integar
        # Start at the head node
        node = self.head # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None: # Always n interations because no early exit
            # Count one for this node
            node_count += 1 # 0(1)
            # Skip to the next node
            node = node.next # 0(1)
        # Now node_count contains the number of nodes
        return node_count # 0(1)

    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: 0(1) if the index is near the beginning of the list
        Worst case running time: 0(n) if the item is near the tail of the list """
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # Find the node at the given index and return its data
        # check if given index is the head
        if index == 0:
            return self.head.data
        # check if given index is the tail
        elif index == self.size -1:
            return self.tail.data
        else:
            # call item method
            items = self.items() # Theta(n)
            # return item at given index in items
            return items[index] # 0(n)

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: 0(1) if the index is the first or last node.
        Worst case running time: 0(n) if the item is near tail of the list"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # Find the node before the given index and insert item after it
        # create a counter set it to negative 1
        node_counter = -1 # Constant time to assign a variable
        # start at the head
        node = self.head # Constant time to assign a variable reference
        # If there is no first node append it to the list
        if node == None: # Constant time to compare values
            self.append(item)
            return # Constant time to break out of function
        # check of the given index is equal to 0
        if index == 0: # Constant time to compare values
            # prepend new node
            self.prepend(item) # Prepend takes constant time
            return # Constant time to break out of function
        # Check if the given index is equal to the size
        if index == self.size: # Constant time to compare values
            # append the new node
            self.append(item) # Append takes constant time
            return # Constant time to break out of function

        # Initialize the previous node index
        prev_node_index = 0 # Constant time to assign a variable
        # Set to the index of the node before the given index
        prev_node_index = index - 1 # Constant time to assign a variable
        # Initialize the previous node
        prev_node = None
        # Get to the node right before the node at the given index
        while node is not None: # Up to n iterations if we don't exit early
            # increment counter by 1
            node_counter += 1 # Constant time to reassign a variable
            # check if the counter is equal to the given index
            if node_counter == prev_node_index: # Constant time to compare values
                prev_node = node # Constant time to reassign a variable
                # create a new node to hold the given item
                new_node = Node(item) # Constant time to assign a variable
                # set the new node.next to previous node.next
                new_node.next = prev_node.next # Constant time to reassign a variable
                # set previous to new_node.next
                prev_node.next = new_node # Constant time to reassign a variable
                # New node is added increment size
                self.size += 1 # Constant time to reassign a variable
                return # Constant time to break out of function
            # otherwise go to next node
            node = node.next # Constant time to reassign a variable

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Best and worst case running time: O(1) because we ony change the last
        node and never loop through all nodes."""
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            self.head = new_node
        else:
            # Otherwise insert new node after tail
            self.tail.next = new_node
        self.size += 1
        # Update tail to new node regardless
        self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best and worst case running time: O(1) because we ony change the first
        node and never loop through all nodes."""
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
        else:
            # Otherwise insert new node before head
            new_node.next = self.head
        self.size += 1
        # Update head to new node regardless
        self.head = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Up to n iterations if we don't exit early
            # Check if this node's data satisfies the given quality function
            if quality(node.data):  # Constant time to call quality function
                # We found data satisfying the quality function, so exit early
                return node.data  # Constant time to return data
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # We never found data satisfying quality, but have to return something
        return None  # Constant time to return None

    def replace(self, old_item, new_item):
        """Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # Find the node containing the given old_item and replace its
        # data with new_item, without creating a new node object
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # tranverse nodes
        while node is not None: # Up to n iterations if we don't exit early
            # check if node data matches old item
            if node.data == old_item: # Constant time to compare values
                # assign new_item to node.data
                node.data = new_item # Constant time to reassign a variable
                # Break out of function
                return # Constant time to break out of function
            # Otherwise go to the next node
            node = node.next # Constant time to reassign a variable
        else: # If the old item is not found raise a value error
            raise ValueError('Old item not found : {}'.format(old_item))


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list"""
        # Start at the head node
        node = self.head
        # Keep track of the node before the one containing the given item
        previous = None
        # Create a flag to track if we have found the given item
        found = False
        # Loop until we have found the given item or the node is None
        while not found and node is not None:
            # Check if the node's data matches the given item
            if node.data == item:
                # We found data matching the given item, so update found flag
                found = True
            else:
                # Skip to the next node
                previous = node
                node = node.next
        # Check if we found the given item or we never did and reached the tail
        if found:
            # Check if we found a node in the middle of this linked list
            if node is not self.head and node is not self.tail:
                # Update the previous node to skip around the found node
                previous.next = node.next
                # Unlink the found node from its next node
                node.next = None
            # Check if we found a node at the head
            if node is self.head:
                # Update head to the next node
                self.head = node.next
                # Unlink the found node from the next node
                node.next = None
            # Check if we found a node at the tail
            if node is self.tail:
                # Check if there is a node before the found node
                if previous is not None:
                    # Unlink the previous node from the found node
                    previous.next = None
                # Update tail to the previous node regardless
                self.tail = previous
            self.size -= 1
        else:
            # Otherwise raise an error to tell the user that delete has failed
            raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
    # ll = LinkedList(['A', 'B', 'C'])
    # ll.replace('C', '3')
    # print(ll)
