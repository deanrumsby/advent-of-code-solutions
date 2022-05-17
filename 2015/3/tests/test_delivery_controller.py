import unittest
from classes.delivery_controller import DeliveryController

class TestDeliveryController(unittest.TestCase):
    def test_how_many_visited_example1(self):
        dc = DeliveryController()
        dc.load_directions('tests/examples/example1.txt')
        dc.deliver_presents()
        self.assertEqual(dc.how_many_visited(), 2)

    def test_how_many_visited_example2(self):
        dc = DeliveryController()
        dc.load_directions('tests/examples/example2.txt')
        dc.deliver_presents()
        self.assertEqual(dc.how_many_visited(), 4)

    def test_how_many_visited_example3(self):
        dc = DeliveryController()
        dc.load_directions('tests/examples/example3.txt')
        dc.deliver_presents()
        self.assertEqual(dc.how_many_visited(), 2)