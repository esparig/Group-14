"""
Assignment 6: Rearranging cars
"""
from typing import List
import unittest


class ParkingState(dict):
    """
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

    def rearrange_basic(self, end_state, history):
        """Compute any combination of moves to rearrange cars in the end_state order.
        """
        if self == end_state:
            return history
        else:
            for parking_spot, car_id in self.items():
                if self.inverse[car_id] != end_state.inverse[car_id]:
                    new_state = ParkingState(self.copy())
                    new_state[parking_spot], new_state[self.inverse[0]] = 0, car_id
                    if new_state not in history:
                        print(f"Move car #{car_id} from space {self.inverse[car_id]} to {self.inverse[0]}")
                        history.append(new_state)
                        return new_state.rearrange_basic(end_state, history)
                    
    def rearrange_least_moves(self, end_state, history):
        """Compute moves to rearrange cars in the end_state order, using the optimal number of 
        moves computed using induction.
        """
        if self == end_state: # Check if all cars are already in the correct position.
            return history
        current_state = ParkingState(self.copy())
        if  self.inverse[0] == end_state.inverse[0]: # self.inverse[0] is the empty space of the parking
            # We need to move any misplaced car to the empty parking space, 
            # adding 1 move to the solution.
            for parking_spot, car_id in self.items():
                if self.inverse[car_id] != end_state.inverse[car_id]:
                    new_state = ParkingState(self.copy())
                    new_state[parking_spot], new_state[self.inverse[0]] = 0, car_id
                    if new_state not in history:
                        print(f"Move car #{car_id} from space {self.inverse[car_id]} to {self.inverse[0]}")
                        history.append(new_state)
                        current_state = new_state
                break
            
        while current_state[end_state.inverse[0]] != 0:
            # By induction, choosing the car that has to occupy the empty parking space, 
            # the solution is reached in n moves, where n = number of cars.
            car_id = end_state[current_state.inverse[0]]
            move_from, move_to = current_state.inverse[car_id], current_state.inverse[0]
            new_state = ParkingState(current_state.copy())
            new_state[move_from], new_state[move_to] = 0, car_id
            if new_state not in history:
                print(f"Move car #{car_id} from space {new_state.inverse[car_id]} to {new_state.inverse[0]}")
                history.append(new_state)
                current_state = new_state

        return history

class TestParkingRearrangement(unittest.TestCase):

    def test_rearrange_basic(self):
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



    def test_restrictions(self):
        restrictions = {'A': [1, 2], 'D': [2, 3]}
        pass
