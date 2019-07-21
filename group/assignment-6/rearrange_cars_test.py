import unittest
import rearrange_cars

class TestRearrangeCars(unittest.TestCase):

    def test_correct_rearrange(self):
        start_state = {3: 'A', 1: 'B', 2: 'C', 0: 'D'}
        end_state = {1: 'A', 2: 'B', 0: 'C', 3: 'D'}
        rearrange_cars.rearrange_cars(start_state, end_state)

        self.assertEqual(start_state, end_state)
        
    def test_move(self)
        start_state = {3: 'A', 1: 'B', 2: 'C', 0: 'D'}
        rearrange_cars.move(start_state, 3)
        self.assertEqual(start_state, {3: 'D', 1: 'B', 2: 'C', 0: 'A'})

        
        
