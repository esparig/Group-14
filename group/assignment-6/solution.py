"""
Rearranging cars from a random position to a pre-defined position.
"""
from typing import List
import unittest


class ParkingState(dict):
    def __repr__(self):
        return f"{type(self).__name__}({super().__repr__()})"


def rearrange(start_state: ParkingState, end_state: ParkingState, history: List[ParkingState]) -> List[ParkingState]:
    if start_state == end_state:
        return history
    else:
        for parking_spot, car_id in start_state.items():
            if start_state[parking_spot]:
                if end_state[parking_spot] != car_id:
                    new_state = start_state.copy()
                    new_state[parking_spot] = None
                    empty_keys = {key for key, value in start_state.items() if not value}
                    new_state[empty_keys.pop()] = car_id
                    if new_state not in history:
                        history.append(new_state)
                        return rearrange(new_state, end_state, history)


class TestParkingRearrangement(unittest.TestCase):

    def test_simple_solution(self):
        car_ids = {1, 2, 3}
        spot_ids = {'A', 'B', 'C', 'D'}

        start_state = ParkingState({'A': 1, 'B': 2, 'C': None, 'D': 3})
        end_state = ParkingState({'A': 3, 'B': 1, 'C': 2, 'D': None})

        movement_history = rearrange(start_state, end_state, list())

        self.assertEqual(movement_history[-1], end_state)
