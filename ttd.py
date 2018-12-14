import unittest
from oop import Andela35


class TestCohort(unittest.TestCase):
    def test_attendees(self):
        andela35dec = Andela35(70, 'Dec', 5, '3')
        self.assertIs(type(andela35dec.duration), int)
