import unittest
from classes.floorfinder import FloorFinder

class TestFloorFinder(unittest.TestCase):
    def test_final_floor_example1(self):
        f = FloorFinder(0)
        f.load_instructions('tests/examples/p1-1.txt')
        self.assertEqual(f.final_floor(), 0)

    def test_final_floor_example2(self):
        f = FloorFinder(0)
        f.load_instructions('tests/examples/p1-2.txt')
        self.assertEqual(f.final_floor(), 0)

    def test_final_floor_example3(self):
        f = FloorFinder(0)
        f.load_instructions('tests/examples/p1-3.txt')
        self.assertEqual(f.final_floor(), 3)

    def test_final_floor_example4(self):
        f = FloorFinder(0)
        f.load_instructions('tests/examples/p1-4.txt')
        self.assertEqual(f.final_floor(), 3)

    def test_final_floor_example5(self):
        f = FloorFinder(0)
        f.load_instructions('tests/examples/p1-5.txt')
        self.assertEqual(f.final_floor(), 3)

    def test_final_floor_example6(self):
        f = FloorFinder(0)
        f.load_instructions('tests/examples/p1-6.txt')
        self.assertEqual(f.final_floor(), -1)

    def test_final_floor_example7(self):
        f = FloorFinder(0)
        f.load_instructions('tests/examples/p1-7.txt')
        self.assertEqual(f.final_floor(), -1)

    def test_final_floor_example8(self):
        f = FloorFinder(0)
        f.load_instructions('tests/examples/p1-8.txt')
        self.assertEqual(f.final_floor(), -3)

    def test_final_floor_example9(self):
        f = FloorFinder(0)
        f.load_instructions('tests/examples/p1-9.txt')
        self.assertEqual(f.final_floor(), -3)

    def test_position_of_first_entry_example1(self):
        f = FloorFinder(0)
        f.load_instructions('tests/examples/p2-1.txt')
        self.assertEqual(f.position_of_first_entry(-1), 1)

    def test_position_of_first_entry_example2(self):
        f = FloorFinder(0)
        f.load_instructions('tests/examples/p2-2.txt')
        self.assertEqual(f.position_of_first_entry(-1), 5)