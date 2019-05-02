#!python

from set import Set
import unittest


class SetTest(unittest.TestCase):

    def test_init(self):
        s = Set()
        assert s.size == 0

    def test_contains(self):
        s = Set([1, 2, 3])
        assert s.size == 3
        assert s.contains(2) is True

    def test_add(self):
        s = Set([1, 2, 3])
        s.add(3)
        s.add(4)
        s.add(5)
        assert s.size == 5

    def test_remove(self):
        s = Set([4, 5, 8])
        s.add(6)
        s.remove(5)
        assert s.size == 3
        with self.assertRaises(KeyError):
            s.remove(3)  # Key does not exist

    def test_union(self):
        s = Set([4, 5, 8])
        assert s.size == 3
        other_set = Set([9, 10, 8])
        s.union(other_set) == [4, 8, 5, 9, 10]

    def test_intersection(self):
        s = Set([4, 5, 8])
        assert s.size == 3
        other_set = Set([4, 6, 8])
        s.intersection(other_set) == [4, 8]

    def test_difference(self):
        s = Set([4, 5, 8, 11])
        assert s.size == 4
        other_set = Set([4, 6, 8])
        s.difference(other_set) == [5, 6, 11]
