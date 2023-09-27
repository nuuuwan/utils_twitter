from unittest import TestCase

from utils_twitterimport Tweet


class TestTweet(TestCase):
    def test_init(self):
        self.assertIsNotNone(Tweet('test'))
