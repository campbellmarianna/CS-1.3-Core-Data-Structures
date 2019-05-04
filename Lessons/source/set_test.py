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

    def test_contains(self):
        s = Set([4, 5, 6, 7, 8])
        assert s.size == 5
        assert s.contains(9) is False

    def test_contains(self):
        s = Set([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        assert s.size == 12
        assert s.contains(20) is True

    def test_add(self):
        s = Set(['a', 'b', 'c'])
        s.add(3)
        s.add(4)
        s.add(5)
        assert s.size == 6

    def test_add(self):
        s = Set(['a', 'b', 'c'])
        s.add('d')
        s.add('f')
        assert s.size == 5
        s.add('g')
        s.add('x')
        s.add('y')
        s.add('z')
        assert s.size == 9

    def test_add(self):
        s = Set()
        s.add('luke')
        s.add('jack')
        assert s.size == 2

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
        assert s.union(other_set).size == 5

    def test_union(self):
        s = Set([])
        assert s.size == 0
        other_set = Set([9, 10, 8])
        assert s.union(other_set).size == 3

    def test_union(self):
        s = Set([4, 5, 8, 3, 6, 7])
        assert s.size == 6
        other_set = Set([9, 10, 8])
        assert s.union(other_set).size == 8

    def test_intersection(self):
        s = Set([4, 5, 8])
        assert s.size == 3
        other_set = Set([4, 6, 8])
        assert s.intersection(other_set).size == 2

    def test_intersection(self):
        s = Set([1, 2])
        assert s.size == 2
        other_set = Set([4, 6, 8])
        assert s.intersection(other_set).sie == 0

    def test_intersection(self):
        s = Set([7, 8, 9, 10])
        assert s.size == 4
        other_set = Set([10, 9, 8, 7])
        assert s.intersection(other_set).size == 4

    def test_difference(self):
        s = Set([4, 5, 8, 11])
        assert s.size == 4
        other_set = Set([4, 6, 8])
        assert s.difference(other_set).size == 2

    def test_difference(self):
        s = Set([])
        assert s.size == 0
        other_set = Set([4, 5])
        assert s.difference(other_set).size == 0

    def test_difference(self):
        s = Set([2, 11])
        assert s.size == 2
        other_set = Set([4, 6, 8])
        assert s.difference(other_set).size == 5

    def test_is_subset(self):
        s = Set([4, 5, 9, 8])
        assert s.size == 4
        other_set = Set([5, 9])
        assert s.is_subset(other_set) == True

    def test_is_subset(self):
        s = Set([4, 5, 9, 8, 1, 2,])
        assert s.size == 6
        other_set = Set([3])
        assert s.is_subset(other_set) == False

    def test_is_subset(self):
        s = Set([72, 89, 35, 65, 81])
        # assert s.size == 3
        other_set = Set([66, 77, 89, 72, 81, 35, 65])
        assert s.is_subset(other_set) is False
