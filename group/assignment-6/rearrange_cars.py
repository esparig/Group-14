"""
Assignment 6: Rearranging cars
Rearrange cars from a state to a end_state.
Assumptions:
- Parking spots are labeled using strings
- Cars are identified by integers
- The number 0 indicates that there is no car in that spot
"""
from typing import List
import copy
import sys
from random import randrange
from util import window

class ParkingState(dict):
    """
    Class to define the state of the parking using a dictionary.
    Represented by a mapping from car to parking_lot.
    Assumptions: input state can be mutated
    """
    def __init__(self, mapping: dict, reserved_for: dict = {}):
        super(ParkingState, self).__init__(mapping)
        self.inverse = {}
        for key, value in self.items():
            self.inverse.__setitem__(value, key)
        self.restrictions = self.__get_restrictions__(reserved_for)

    def __setitem__(self, key, value):
        super(ParkingState, self).__setitem__(key, value)
        self.inverse.__setitem__(value, key)

    def __delitem__(self, key):
        self.inverse.__delitem__(self[key])
        super(ParkingState, self).__delitem__(key)

    def __repr__(self):
        return "{0}({1})".format(type(self).__name__, super().__repr__())

    def __get_restrictions__(self, reserved_for):
        # Restrictions are the cars not allowed in a certain space i.e.
        # all other cars that are not reserved for this space
        return {lot_id: (set(range(1, len(self))) - set(reserved_for[lot_id])) if lot_id in reserved_for else set()
                for car_id, lot_id in self.items()}

    def move_car(self, car_id: int):
        """
        Moves a car from its current parking lot to the empty lot
        @car_id: a car which is leaving its current lot to be moved to currently empty lot
        """
        self[0], self[car_id] = self[car_id], self[0]

    # Do not access inverse directly, wrap it in a method
    def find_car_given_lot(self, lot_id):
        """
        Finds the car that's currently in a given parking lot via inverse lookup.
        :param lot_id: Lot to find car in
        :return: Car in lot lot_id
        """
        return self.inverse[lot_id]

    def rearrange_cars_any_path(self, end_state: 'ParkingState', history: List['ParkingState'] = []) \
            -> List:
        """
        Rearranges cars from start_state into end_state.
        Assumptions:
            - configurations (i.e. intermediate parking lot states) do not have to be unique
            - the sequence returned does not need to minimise the number of swaps
            - restrictions, if provided, apply to intermediate states
        :param end_state: goal parking lot configuration
        :param history: a list of past parking lot configurations / states
        :return: Returns a sequence of configurations representing a path from start_state to end_state.
        """
        history = history + [copy.deepcopy(self)]
        while self != end_state:
            if self[0] == end_state[0]:
                # If there is a deadlock because of restrictions and the goal empty lot is currently empty,
                # move a random car to the empty spot
                if self[0] == end_state[0]:
                    car_id = randrange(1, len(self))
                    self.move_car(car_id)
                    # append current state to history list
                    history.append(copy.deepcopy(self))
            # For every car in lot, check that it's not yet in its correct lot and that it can be moved to the empty lot
            for car_id in range(1, len(self)):
                if self[car_id] != end_state[car_id] and car_id not in self.restrictions[self[0]]:
                    self.move_car(car_id)
                    # append current state to history list
                    history.append(copy.deepcopy(self))
        return history

    # shortest
    def rearrange_cars_shortest_path(self, end_state: 'ParkingState', history: List['ParkingState'] = []) \
            -> List:
        """
        Rearranges cars from start_state into end_state.
        Assumptions:
            - configurations (i.e. intermediate parking lot states) do not have to be unique
            - the sequence returned does need to minimise the number of swaps
            - restrictions, if provided, apply to intermediate states
        :param end_state: goal parking lot configuration
        :param history: a list of past parking lot configurations / states
        :return: Returns the shortest sequence of configurations representing a path from start_state to end_state.
        """
        history = history + [copy.deepcopy(self)]

        while self != end_state:
            # if the lot that should be empty already is empty, swap it with a random car that needs to be moved
            if self[0] == end_state[0]:
                car_to_move = [car_id for car_id in self if
                               car_id in end_state and self[car_id] != end_state[car_id]
                               and car_id not in self.restrictions[self[0]]].pop()
                self.move_car(car_to_move)
                # append current state to history list
                history.append(copy.deepcopy(self))
            # find the car that needs to go to the empty lot, then move it there
            car_to_move = end_state.find_car_given_lot(self[0])
            self.move_car(car_to_move)
            # append current state to history list
            history.append(copy.deepcopy(self))
        return history

    def rearrange_cars_all_paths_distinct_states(self, end_state: 'ParkingState', history: List['ParkingState'] = []) \
            -> List:
        """
        Rearranges cars from start_state into end_state in all possible ways as long as intermediate states in a sequence
        are distinct.
        Assumptions:
            - configurations (i.e. intermediate parking lot states) do have to be unique
            - restrictions, if provided, apply to intermediate states
        :param end_state: goal parking lot configuration
        :param history: a list of past parking lot configurations / states
        :return: A list of all possible sequences of states between start and end state whereintermediate states in a sequence
        are distinct.
        """
        history = history + [copy.deepcopy(self)]
        if self == end_state:
            # If end state is reached return one possible sequence of states
            return [history]
        histories = []
        # Any car could go into empty space on every turn. For each car, check if moving it to the empty lot is valid,
        # i.e. parking lot configuration after swap has not been visited yet.
        # If yes, copy history so far and branch off
        for car_id in range(1, len(self)):
            if self[car_id] != end_state[car_id] and car_id not in self.restrictions[self[0]]:
                swap_state = copy.deepcopy(self)
                swap_state.move_car(car_id)
                if swap_state not in history:
                    branches = swap_state.rearrange_cars_all_paths_distinct_states(end_state, history)
                    for branch in branches:
                        histories.append(branch)
        return histories

    def violates_constraints(self):
        """
        Check if current state violates constraints.
        :return: bool indicating if constraints are violated
        """
        violates = False
        for car, parking_lot in self.items():
            if car in self.restrictions[parking_lot]:
                violates = True
                break
        return violates

    def path_to_satisfying_end_state(self, history: List['ParkingState'] = []):
        """
        Given a set of constraints, return any end state that satisfies them.
        Assumptions:
            - configurations (i.e. intermediate parking lot states) do not have to be unique
            - restrictions, if provided, do not apply to intermediate states
        :param history: parking lot configurations so far
        :return: Sequence of parking lot configurations leading to a satisfying end state
        """
        history = history + [copy.deepcopy(self)]
        while self.violates_constraints(): # Move cars until constrains are no longer violated
            for car_id in range(1, len(self)):
                self.move_car(car_id)
                history.append(copy.deepcopy(self))
            # if it still violates constrains, move a random car to get out of loop
            if self.violates_constraints():
                car_id = randrange(1, len(self))
                self.move_car(car_id)
                # append current state to history list
                history.append(copy.deepcopy(self))
        return history

    def __print_moves__(self, sequences: List['ParkingState']):
        """
        For a given list of sequences, print moves.
        :param sequences: list of sequences from start_state to end_state
        """
        for seq_pair in sequences:
            car_moved = seq_pair[0].find_car_given_lot(seq_pair[1][0])
            yield ("Move car {0} from lot {1} to empty space at lot {2}".format(car_moved, seq_pair[1][0],
                                                                               seq_pair[0][0]))

    # Printing helpers.
    def print_any_path(self, end_state: 'ParkingState'):
        path = self.rearrange_cars_any_path(end_state)
        if len(path) > 1:
            print("A move sequence to arrange cars in given state: ")
            [print(move) for move in self.__print_moves__(list(window(path)))]
        elif self.violates_constraints():
            raise Exception("There are no move sequences that satisfy there requirements.")
        elif self == end_state:
            raise Exception("Start and end state are the same.")

    def print_shortest_path(self, end_state: 'ParkingState'):
        path = self.rearrange_cars_shortest_path(end_state)
        if len(path) > 1:
            print("Shortest move sequence to arrange cars in given state:: ")
            [print(move) for move in self.__print_moves__(list(window(path)))]
        elif self.violates_constraints():
            raise Exception("There are no move sequences that satisfy there requirements.")
        elif self == end_state:
            raise Exception("Start and end state are the same.")

    def print_all_paths(self, end_state: 'ParkingState'):
        paths = self.rearrange_cars_all_paths_distinct_states(end_state)
        if len(paths) > 1:
            for i in range(0, len(paths)):
                print("Move sequence to arrange cars in given state #{0}:".format(i+1))
                sequences = [seq for seq in window(paths[i])]
                [print(move) for move in self.__print_moves__(sequences)]
        elif self.violates_constraints():
            raise Exception("There are no move sequences that satisfy there requirements.")
        elif self == end_state:
            raise Exception("Start and end state are the same.")

    def print_path_to_satisfying_end_state(self):
        path = self.path_to_satisfying_end_state()
        if len(path) > 1:
            print("Move sequence to arrange cars in state {0}, which satisfies constraints: ".format(path[-1]))
            [print(move) for move in self.__print_moves__(list(window(path)))]
        elif self.violates_constraints():
            raise Exception("There are no move sequences that satisfy there requirements.")
        elif self == path[-1]:
            raise Exception("Start and end state are the same.")

def main(args):
    start_state = ParkingState({0: 'C', 1: 'A', 2: 'B', 3: 'D'})
    end_state = ParkingState({0: 'B', 1: 'C', 2: 'A', 3: 'D'})
    start_state.print_any_path(end_state)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
