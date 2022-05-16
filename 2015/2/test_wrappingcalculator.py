import unittest
from wrappingcalculator import WrappingCalculator

class TestWrappingCalculator(unittest.TestCase):
    def test_surface_area_example1(self):
        w = WrappingCalculator()
        self.assertEqual(w.surface_area([2, 3, 4]), 52)

    def test_smallest_side_area_example1(self):
        w = WrappingCalculator()
        self.assertEqual(w.smallest_side_area([2, 3, 4]), 6)

    def test_wrapping_paper_req_example1(self):
        w = WrappingCalculator()
        self.assertEqual(w.wrapping_paper_req([2, 3, 4]), 58)

    def test_surface_area_example2(self):
        w = WrappingCalculator()
        self.assertEqual(w.surface_area([1, 1, 10]), 42)

    def test_smallest_side_area_example2(self):
        w = WrappingCalculator()
        self.assertEqual(w.smallest_side_area([1, 1, 10]), 1)

    def test_wrapping_paper_req_example2(self):
        w = WrappingCalculator()
        self.assertEqual(w.wrapping_paper_req([1, 1, 10]), 43)

    def test_smallest_perimeter_example1(self):
        w = WrappingCalculator()
        self.assertEqual(w.smallest_perimeter([2, 3, 4]), 10)

    def test_ribbon_bow_length_example1(self):
        w = WrappingCalculator()
        self.assertEqual(w.ribbon_bow_length([2, 3, 4]), 24)

    def test_ribbon_req_example1(self):
        w = WrappingCalculator()
        self.assertEqual(w.ribbon_req([2, 3, 4]), 34)


if __name__ == "__main__":
    unittest.main()