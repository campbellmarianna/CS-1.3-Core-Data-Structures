#!python

from set import Set
import unittest


class SetTest(unittest.TestCase):

    def test_init(self):
        s = Set()
        assert s.size == 0
