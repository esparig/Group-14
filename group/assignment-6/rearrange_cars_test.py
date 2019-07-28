import unittest
import rearrange_cars
from rearrange_cars import ParkingState

class TestRearrangeCars(unittest.TestCase):

    def test_correct_rearrange(self):
        start_state = ParkingState({3: 'A', 1: 'B', 2: 'C', 0: 'D'},
                                   reserved_for={'A': [0, 1, 2, 3], 'B': [0, 1, 2, 3], 'C': [0, 1], 'D': [0, 2, 3]})
        end_state = ParkingState({1: 'A', 2: 'B', 0: 'C', 3: 'D'})

        history = start_state.rearrange_cars_any_path(end_state)
        self.assertEqual(start_state, end_state)
        
    def test_move(self):
        pass
        start_state = {3: 'A', 1: 'B', 2: 'C', 0: 'D'}
        #rearrange_cars.move(start_state, 3)
        #self.assertEqual(start_state, {3: 'D', 1: 'B', 2: 'C', 0: 'A'})

        
        
