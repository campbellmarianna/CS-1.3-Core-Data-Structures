#!python
from redact_problem import redact_words
import unittest


class SetTest(unittest.TestCase):

    def test_redact_words_easy_input(self):
        assert redact_words(['fluffy', 'bad'], ['bad']) == ['fluffy']

    def test_redact_words_medium_input(self):
        assert redact_words(['fluffy', 'bad', 'superbad', 'good'], ['bad', 'superbad']) == ['fluffy', 'good']

    def test_redact_words_hard_input(self):
        assert redact_words(['fluffy', 'bad', 'supergood', 'horriable', 'really bad'], ['bad', 'horriable', 'really bad']) == ['fluffy', 'supergood']
