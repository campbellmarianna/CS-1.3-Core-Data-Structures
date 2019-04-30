#!python

from linkedlist import LinkedList
import copy

class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = [LinkedList() for i in range(init_size)]
        self.size = 0  # Number of key-value entries

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def load_factor(self):
        """Return the load factor, the ratio of number of entries to buckets.
        Best and worst case running time: O(n) for n LinkedList in the array and
        get the length."""
        # Calculate load factor                   # Inspired by Faith Chikwekwe
        if len(self.buckets) == 0:
            raise AssertionError("HashTable is empty.")
        print(self.size, len(self.buckets), self.size/len(self.buckets))
        return self.size / len(self.buckets) # O(n)/(1)

    def keys(self):
        """Return a list of all keys in this hash table.
        Best and worst case running time: O(b + n) for b buckets in the LinkedList
        because we have iterate over all b buckets, iterate over all the n nodes
        and append the key for each"""
        # Collect all keys in each of the buckets
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Best and worst case running time: O(n + n) for b buckets in the LinkedList
        because we have to iterate over all b buckets, iterate over all the n nodes
        and append the value for each"""
        # Collect all values in each of the buckets
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all entries (key-value pairs) in this hash table.
        Best and worst case running time: O(n) for n buckets in the array because
        we always need to loop through all n buckets to get there items."""
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Best and worst case running time: O(n) for n LinkedList in the array
        because we have to iterate over all n LinkedList and get the length for each"""
        # Count number of key-value entries in each of the buckets
        item_count = 0
        for bucket in self.buckets: # b interations
            item_count += bucket.length() # O(l)
        return item_count
        # Equivalent to this list comprehension:
        return sum(bucket.length() for bucket in self.buckets)
        # Overall: o(b * 1) --> O(n)

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Best case running time: O(1) if the key is found early in iterating through
        the bucket
        Worst case running time: O(n + i) for n nodes in the LinkedList because
        we have to iterate over all n nodes, iterate over all the i items and check
        to see whose data matches the given key"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        return entry is not None  # True or False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Best case running time: O(1) if the key is found early in iterating through
        the bucket
        Worst case running time: O(n + i) for n nodes in the LinkedList because
        we have to iterate over all n nodes, iterate over all the i items and check
        to see whose data matches the given key"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Return the given key's associated value
            assert isinstance(entry, tuple)
            assert len(entry) == 2
            return entry[1]
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Best case running time: O(1) item is located near head of list
        Worst case running time: 0(l) (find) + O(l) (delete) = O(l) (delete) =
        O(2*1) simplifies to O(l) if item is near tail of list"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # In this case, the given key's value is being updated
            # Remove the old key-value entry from the bucket first
            bucket.delete(entry)
            # Decrement size
            self.size -= 1
        # Insert the new key-value entry into the bucket in either case
        bucket.append((key, value))
        # Increment size
        self.size += 1
        # Check if the load factor exceeds a threshold such as 0.75
        if self.load_factor() > 0.75:
            # If so, automatically resize to reduce the load factor
            self._resize()

    def delete(self, key):
        """Delete the given key and its associated value, or raise KeyError.
        Best case running time: O(1) item is located near head of list
        Worst case running time: O(n + i) for n nodes in the LinkedList because
        we have to iterate over all n nodes, iterate over all the i items and
        check to see whose data matches the given key"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Remove the key-value entry from the bucket
            bucket.delete(entry) # O(l), delete method is scoped to LinkedList object
            # Decrement size
            self.size -= 1
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))
        # Overall O(3 + 2l) --> O(l)

    def _resize(self, new_size=None):
        """Resize this hash table's buckets and rehash all key-value entries.
        Should be called automatically when load factor exceeds a threshold
        such as 0.75 after an insertion (when set is called with a new key).
        Best and worst case running time: ??? under what conditions? [TODO]
        Best and worst case space usage: ??? what uses this memory? [TODO]"""
        # If unspecified, choose new size dynamically based on current size
        if new_size is None:
            new_size = len(self.buckets) * 2  # Double size
        # Option to reduce size if buckets are sparsely filled (low load factor)
        elif new_size is 0:
            new_size = len(self.buckets) / 2  # Half size
        # Get a list to temporarily hold all current key-value entries
        temp_list = self.items() # a list of all entries (key-value pairs)
        # Create a new list of new_size total empty linked list buckets
        self.buckets = [LinkedList() for i in range(new_size)]
        self.size = 0  # Number of key-value entries
        # Insert each key-value entry into the new list of buckets,
        # which will rehash them into a new bucket index based on the new size
        for key, value in temp_list:
            # print("Old Entry:", old_entry)
            # print("Old Entry Key:", old_entry[0])
            # print("Old Entry Value:", old_entry[1])
            self.set(key, value)


def test_hash_table():
    ht = HashTable(4)
    print('HashTable: ' + str(ht))

    print('Setting entries:')
    ht.set('I', 1)
    print('set(I, 1): ' + str(ht))
    ht.set('V', 5)
    print('set(V, 5): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))
    ht.set('X', 10)
    print('set(X, 10): ' + str(ht))
    ht.set('L', 50)  # Should trigger resize
    print('set(L, 50): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))

    print('Getting entries:')
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('get(L): ' + str(ht.get('L')))
    print('contains(X): ' + str(ht.contains('X')))
    print('contains(Z): ' + str(ht.contains('Z')))

    print('Deleting entries:')
    ht.delete('I')
    print('delete(I): ' + str(ht))
    ht.delete('V')
    print('delete(V): ' + str(ht))
    ht.delete('X')
    print('delete(X): ' + str(ht))
    ht.delete('L')
    print('delete(L): ' + str(ht))
    print('contains(X): ' + str(ht.contains('X')))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))


if __name__ == '__main__':
    test_hash_table()
