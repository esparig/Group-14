"""
Assignment 6: Rearranging cars

Rearrange cars from a state to a end_state.

Assumptions:
- Parking spots are labeled using strings
- Cars are identified by integers
- The number 0 indicates that there is no car in that spot
"""
from typing import List
import unittest


class ParkingState(dict):
    """Class to define the state of the parking using a dictionary.
    To access to the location of the cars use the inverse dictionary.
    """
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

    def move_car(self, car_id: int, parking_spot: str,
                 history: List['ParkingState']) -> 'ParkingState':
        """Move car_id to parking_spot and returns a new state of the Parking
        """
        new_state = ParkingState(self.copy())
        new_state[parking_spot], new_state[self.inverse[0]] = 0, car_id
        if new_state not in history:
            print(f"Move car #{car_id} from space {self.inverse[car_id]} to {self.inverse[0]}")
            history.append(new_state)
            return new_state

    def rearrange_basic(self, end_state: 'ParkingState',
                        history: List['ParkingState']) -> List['ParkingState']:
        """Compute any combination of moves to rearrange cars in the end_state order.
        """
        if self == end_state:
            return history
        else:
            for parking_spot, car_id in self.items():
                if self.inverse[car_id] != end_state.inverse[car_id]:
                    new_state = self.move_car(car_id, parking_spot, history)
                    if new_state:
                        return new_state.rearrange_basic(end_state, history)

    def rearrange_least_moves(self, end_state: 'ParkingState',
                              history: List['ParkingState']) -> List['ParkingState']:
        """Compute moves to rearrange cars in the end_state order, using the optimal number of
        moves computed using induction.
        """
        if self == end_state: # Check if all cars are already in the correct position.
            return history

        if self.inverse[0] == end_state.inverse[0]:
            # self.inverse[0] indicates the empty space of the parking
            # We need to move any misplaced car to the empty parking space,
            # adding 1 move to the solution.
            for parking_spot, car_id in self.items():
                if self.inverse[car_id] != end_state.inverse[car_id]:
                    current_state = self.move_car(car_id, parking_spot, history)
                break
        else:
            current_state = ParkingState(self.copy())

        while current_state[end_state.inverse[0]] != 0:
            # By induction, choosing the car that has to occupy the empty parking space,
            # the solution is reached in n moves, where n = number of cars.
            car_id = end_state[current_state.inverse[0]]
            parking_spot = current_state.inverse[car_id]
            current_state = current_state.move_car(car_id, parking_spot, history)
        return history

    def rearrange_get_all(self, end_state: 'ParkingState',
                          history: List['ParkingState']) -> List['ParkingState']:
        """Compute all possible combinations of moves to rearrange cars in the end_state order.
        """
        if self == end_state:
            yield history.copy()
        else:
            for parking_spot, car_id in self.items():
                if self.inverse[car_id] != end_state.inverse[car_id]:
                    new_state = ParkingState(self.copy())
                    new_state[parking_spot], new_state[self.inverse[0]] = 0, car_id
                    if new_state not in history:
                        print(f"Move car {car_id} from {self.inverse[car_id]}"
                              f" to {self.inverse[0]}")
                        history.append(new_state)
                        yield from new_state.rearrange_get_all(end_state, history)
                        history.pop(-1)

class TestParkingRearrangement(unittest.TestCase):
    """Test class for assignment 6: Rearranging cars.
    """

    def test_rearrange_basic(self):
        """Test if rearrange basic gives a valid solution.
        """
        print(f"Start test for rearrange_basic:\n-------------------------------")

        start_state = ParkingState({'A': 1, 'B': 2, 'C': 0, 'D': 3})
        end_state = ParkingState({'A': 3, 'B': 1, 'C': 2, 'D': 0})
        movement_history = start_state.rearrange_basic(end_state, list())
        self.assertEqual(movement_history[-1], end_state)

        print(f"-------------------------------\nEnd test for rearrange_basic\n")
        print(f"Start test for rearrange_basic:\n-------------------------------")

        start_state = ParkingState({'A':3, 'B':1, 'C':2, 'D':0})
        end_state = ParkingState({'A':1, 'B':2, 'C':3, 'D':0})
        movement_history = start_state.rearrange_basic(end_state, list())
        self.assertEqual(movement_history[-1], end_state)

        print(f"-------------------------------\nEnd test for rearrange_basic\n")

    def test_rearrange_least_moves(self):
        """Test if rearrange the parking using least number of moves works as expected.
        """
        print(f"Start test for rearrange_least_moves:\n-------------------------------")

        start_state = ParkingState({'A': 1, 'B': 2, 'C': 0, 'D': 3})
        end_state = ParkingState({'A': 3, 'B': 1, 'C': 2, 'D': 0})
        movement_history = start_state.rearrange_least_moves(end_state, list())
        self.assertEqual(movement_history[-1], end_state)

        print(f"-------------------------------\nEnd test for rearrange_least_moves\n")

        print(f"Start test for rearrange_least_moves:\n-------------------------------")

        start_state = ParkingState({'A': 3, 'B': 1, 'C': 2, 'D': 0})
        end_state = ParkingState({'A': 1, 'B': 2, 'C': 3, 'D': 0})
        movement_history = start_state.rearrange_least_moves(end_state, list())
        self.assertEqual(movement_history[-1], end_state)

        print(f"-------------------------------\nEnd test for rearrange_least_moves\n")

    def test_get_all_solutions(self):
        """Test if getting all solutions to rearrange cars works as expected.
        """
        start_state = ParkingState({'A': 1, 'B': 2, 'C': 0, 'D': 3})
        end_state = ParkingState({'A': 3, 'B': 1, 'C': 2, 'D': 0})

        movement_history = [i for i in start_state.rearrange_get_all(end_state, list())]
        num_shortest_solution = sum(1 for i in movement_history if len(i) == 3)
        num_longest_solution = sum(1 for i in movement_history if len(i) == 16)
        self.assertEqual(num_shortest_solution, 1)
        self.assertEqual(num_longest_solution, 2)
        self.assertEqual(len(movement_history), 180)
    '''
    def test_restrictions(self):
        restrictions = {'A': [1, 2], 'D': [2, 3]}
        pass
    '''