"""
Assignment 6: Rearranging cars
Rearrange cars from a state to a end_state.
Assumptions:
- Parking spots are labeled using strings
- Cars are identified by integers
- The number 0 indicates that there is no car in that spot
"""

import unittest
from util import window
from rearrange_cars import ParkingState


class TestParkingRearrangement(unittest.TestCase):
    """Test class for assignment 6: Rearranging cars.
    """

    def test_rearrange_any_path(self):
        """Test if rearrange_cars_any_path gives a valid solution.
        """
        # empty lot already in place
        start_state = ParkingState({0: 'C', 1: 'A', 2: 'B', 3: 'D'})
        end_state = ParkingState({0: 'C', 1: 'B', 2: 'D', 3: 'A'})
        state_history = start_state.rearrange_cars_any_path(end_state)
        # test that last state is end state
        self.assertEqual(state_history[-1], end_state)

        # empty lot not in place
        start_state = ParkingState({0: 'B', 1: 'A', 2: 'C', 3: 'D'})
        end_state = ParkingState({0: 'C', 1: 'B', 2: 'D', 3: 'A'})
        state_history = start_state.rearrange_cars_any_path(end_state)
        # test that last state is end state
        self.assertEqual(state_history[-1], end_state)

        # starting state is the same as ending state
        start_state = ParkingState({0: 'B', 1: 'A', 2: 'C', 3: 'D'})
        end_state = ParkingState({0: 'B', 1: 'A', 2: 'C', 3: 'D'})
        state_history = start_state.rearrange_cars_any_path(end_state)
        # test that last state is end state
        self.assertEqual(state_history[-1], end_state)

    def test_print_moves(self):
        # Since there is a move between each pair of sequences, there should be 1 fewer moves than sequences

        # Any sequence
        start_state = ParkingState({0: 'B', 1: 'A', 2: 'C', 3: 'D'})
        end_state = ParkingState({0: 'C', 1: 'B', 2: 'D', 3: 'A'})
        state_history = start_state.rearrange_cars_any_path(end_state)
        sequences = list(window(state_history))
        move_history = [move for move in start_state.__print_moves__(sequences)]
        self.assertEqual(len(state_history)-1, len(move_history))

        # Same start and end state
        start_state = ParkingState({0: 'B', 1: 'A', 2: 'C', 3: 'D'})
        end_state = ParkingState({0: 'B', 1: 'A', 2: 'C', 3: 'D'})
        state_history = start_state.rearrange_cars_any_path(end_state)
        sequences = list(window(state_history))
        move_history = [move for move in start_state.__print_moves__(sequences)]
        self.assertEqual(len(state_history)-1, len(move_history))

        # Empty is in correct end configuration
        start_state = ParkingState({0: 'B', 1: 'A', 2: 'C', 3: 'D'})
        end_state = ParkingState({0: 'B', 1: 'C', 2: 'D', 3: 'A'})
        state_history = start_state.rearrange_cars_any_path(end_state)
        sequences = list(window(state_history))
        move_history = [move for move in start_state.__print_moves__(sequences)]
        self.assertEqual(len(state_history)-1, len(move_history))

        # Shortest sequence
        start_state = ParkingState({0: 'B', 1: 'A', 2: 'C', 3: 'D'})
        end_state = ParkingState({0: 'C', 1: 'B', 2: 'D', 3: 'A'})
        state_history = start_state.rearrange_cars_shortest_path(end_state)
        sequences = list(window(state_history))
        move_history = [move for move in start_state.__print_moves__(sequences)]
        self.assertEqual(len(state_history)-1, len(move_history))

        # Constraints on end configuration
        start_state = ParkingState({0: 'B', 1: 'A', 2: 'C', 3: 'D'}, reserved_for={'C': [1]})
        state_history = start_state.path_to_satisfying_end_state()
        sequences = list(window(state_history))
        move_history = [move for move in start_state.__print_moves__(sequences)]
        self.assertEqual(len(state_history)-1, len(move_history))

    def test_rearrange_cars_shortest_path(self):
        """Test if rearrange the parking using least number of moves works as expected.
        """

        # empty lot already in place
        start_state = ParkingState({0: 'D', 1: 'B', 2: 'C', 3: 'A'})
        end_state = ParkingState({0: 'D', 1: 'A', 2: 'B', 3: 'C'})
        movement_history = start_state.rearrange_cars_shortest_path(end_state)
        self.assertEqual(movement_history[-1], end_state)

        # empty lot not in place
        start_state = ParkingState({0: 'C', 1: 'A', 2: 'B', 3: 'D'})
        end_state = ParkingState({0: 'D', 1: 'B', 2: 'C', 3: 'A'})
        movement_history = start_state.rearrange_cars_shortest_path(end_state)
        self.assertEqual(movement_history[-1], end_state)

    def test_get_all_solutions(self):
        """Test if getting all solutions to rearrange cars works as expected.
        """
        # empty lot not in place
        start_state = ParkingState({0: 'C', 1: 'A', 2: 'B', 3: 'D'})
        end_state = ParkingState({0: 'D', 1: 'B', 2: 'C', 3: 'A'})

        movement_history = start_state.rearrange_cars_all_paths_distinct_states(end_state)
        self.assertEqual(len(movement_history), 62)

    def test_restrictions(self):
        # There is a restrictions entry for each lot
        start_state = ParkingState({0: 'C', 1: 'A', 2: 'B', 3: 'D'}, reserved_for={'C': [1]})
        self.assertEqual(len(start_state.restrictions), len(start_state))
        # 'C' is reserved for car 1, so it should have 2 and 3 in its restrictions
        self.assertEqual(start_state.restrictions['C'], {2, 3})
        # 'A', 'B' and 'D' have no restrictions
        self.assertEqual(start_state.restrictions['A'], set())
        self.assertEqual(start_state.restrictions['B'], set())
        self.assertEqual(start_state.restrictions['D'], set())

    def test_violates_constraints(self):
        # 'C' is reserved for car 1, and is now empty, so this state should not be invalid
        start_state = ParkingState({0: 'C', 1: 'A', 2: 'B', 3: 'D'}, reserved_for={'C': [1]})
        self.assertFalse(start_state.violates_constraints())

        # 'C' is reserved for car 1, and is now not empty, so this state should be invalid
        start_state = ParkingState({0: 'B', 1: 'A', 2: 'C', 3: 'D'}, reserved_for={'C': [1]})
        self.assertTrue(start_state.violates_constraints())

        # 'C' is reserved for car 1, and car 1 is parked in 'C', so this state should not be invalid
        start_state = ParkingState({0: 'A', 1: 'C', 2: 'B', 3: 'D'}, reserved_for={'C': [1]})
        self.assertFalse(start_state.violates_constraints())

    def test_satisfying_solution(self):
        # 'C' is reserved for car 1, and 'A' is reserved for car 3 so this state should not be invalid
        start_state = ParkingState({0: 'C', 1: 'A', 2: 'B', 3: 'D'}, reserved_for={'A': [3], 'C': [1]})
        self.assertTrue(start_state.violates_constraints())
        # Find a satisfying end state
        state_history = start_state.path_to_satisfying_end_state()
        # State should not be invalid
        self.assertFalse(state_history[-1].violates_constraints())
