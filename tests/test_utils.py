import unittest

from api.utils import to_seconds


class TestUtils(unittest.TestCase):
    
    def test_to_seconds(self):
        self.assertEqual(to_seconds("01:00:00"), 3600)
        self.assertEqual(to_seconds("00:30:00"), 1800)
        self.assertEqual(to_seconds("00:01:00"), 60)
        self.assertEqual(to_seconds("00:00:30"), 30)
