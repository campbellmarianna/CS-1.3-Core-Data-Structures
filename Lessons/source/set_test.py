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
        s = Set()
        s.add(3)
        s.add(4)
        s.add(5)
        assert s.size == 3
