"""
Rearranging cars from a random position to a pre-defined position.
"""
from typing import List
import unittest


class ParkingState(dict):

    def __init__(self, *args, **kwargs):
        super(ParkingState, self).__init__(*args, **kwargs)
        self.restrictions = kwargs.pop('restrictions', dict())
        self.inverse = {}
        for key, value in self.items():
            self.inverse.__setitem__(value, key)

    def __setitem__(self, key, value):
        super(ParkingState, self).__setitem__(key, value)
        self.inverse.__setitem__(value, key)

    def __delitem__(self, key):
        self.inverse.__delitem__(self[key])
        super(ParkingState, self).__delitem__(key)

    def __repr__(self):
        return f"{type(self).__name__}({super().__repr__()})"

    def rearrange_basic(self, end_state, history):
        if self == end_state:
            return history
        else:
            for parking_spot, car_id in self.items():
                if self.inverse[car_id] != end_state.inverse[car_id]:
                    new_state = ParkingState(self.copy())
                    new_state[parking_spot], new_state[self.inverse[0]] = 0, car_id
                    if new_state not in history:
                        print(f"Move car {car_id} from {self.inverse[car_id]} to {self.inverse[0]}")
                        history.append(new_state)
                        return new_state.rearrange_basic(end_state, history)


class TestParkingRearrangement(unittest.TestCase):

    def test_simple_solution(self):
        start_state = ParkingState({'A': 1, 'B': 2, 'C': 0, 'D': 3})
        end_state = ParkingState({'A': 3, 'B': 1, 'C': 2, 'D': 0})

        movement_history = start_state.rearrange_basic(end_state, list())

        self.assertEqual(movement_history[-1], end_state)

    def test_restrictions(self):
        restrictions = {'A': [1, 2], 'D': [2, 3]}
        pass
