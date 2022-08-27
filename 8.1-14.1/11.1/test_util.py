import unittest
from test_fonction import get_formatted_name

class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name("first", "last")
        # self.assertEqual(formatted_name, "first last")
        self.assertEqual(formatted_name, "first last111")

unittest.main