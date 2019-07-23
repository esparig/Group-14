"""
Rearranging cars from a random position to a pre-defined position.
"""
from typing import List
import unittest


class ParkingState(dict):
    def __repr__(self):
        return f"{type(self).__name__}({super().__repr__()})"

    def change_state(self, end_state: ParkingState, history: List[ParkingState]) -> List[ParkingState]:
        if self == end_state:
            return history
        else:
            for parking_spot, car_id in self.items():
                if self[parking_spot]:
                    if end_state[parking_spot] != car_id:
                        new_state = ParkingState(self.copy())
                        new_state[parking_spot] = None
                        empty_keys = {key for key, value in self.items() if not value}
                        move_to = empty_keys.pop()
                        new_state[move_to] = car_id
                        if new_state not in history:
                            print(f"Move {car_id} from {parking_spot} to {move_to}")
                            history.append(new_state)
                            return new_state.change_state(end_state, history)


class TestParkingRearrangement(unittest.TestCase):

    def test_simple_solution(self):
        car_ids = {1, 2, 3}
        spot_ids = {'A', 'B', 'C', 'D'}

        start_state = ParkingState({'A': 1, 'B': 2, 'C': None, 'D': 3})
        end_state = ParkingState({'A': 3, 'B': 1, 'C': 2, 'D': None})

        movement_history = start_state.change_state(end_state, list())

        self.assertEqual(movement_history[-1], end_state)

    def test_restrictions(self):
        restrictions = {'A': [1, 2], 'D': [2, 3]}
        pass
