import unittest
from classes.santa import Santa

class TestSanta(unittest.TestCase):
    def test_how_many_visited_example1(self):
        s = Santa()
        s.load_directions('tests/examples/example1.txt')
        s.deliver_presents()
        self.assertEqual(s.how_many_visited(), 2)

    def test_how_many_visited_example2(self):
        s = Santa()
        s.load_directions('tests/examples/example2.txt')
        s.deliver_presents()
        self.assertEqual(s.how_many_visited(), 4)

    def test_how_many_visited_example3(self):
        s = Santa()
        s.load_directions('tests/examples/example3.txt')
        s.deliver_presents()
        self.assertEqual(s.how_many_visited(), 2)