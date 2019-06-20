"""Unit tests for Assignment 4: Counting Islands"""
import unittest
from counting_islands import count_islands

MAP1 = [["Sea", "Land", "Sea", "Land"], 
       ["Land", "Land", "Sea", "Sea"],
       ["Sea", "Sea", "Land", "Sea"],
       ["Sea", "Sea", "Land", "Sea"]]

MAP2 = [["Sea", "Sea"],
        ["Sea", "Sea"]]

MAP3 = [["Land", "Land"],
        ["Land", "Land"]]

class TestCountingIslands(unittest.TestCase):
    """Assuming the map is well provided, we test the output of the count_islands function.
    """
    def test_example_map(self):
        num_islands, new_map = count_islands(MAP1)
        self.assertEqual(num_islands, 3, "There are three islands!")
        
    def test_only_sea_map(self):
        num_islands, new_map = count_islands(MAP2)
        self.assertEqual(num_islands, 0, "There isn't any island!")
        
    def test_only_land_map(self):
        num_islands, new_map = count_islands(MAP3)
        self.assertEqual(num_islands, 1, "Maybe we are in a continent!")
        