"""Unit tests for Assignment 4: Counting Islands"""
import unittest
from counting_islands import TypeTerritory, count_islands, count_islands_from_2d_map

MAP1 = [["Sea", "Land", "Sea", "Land"], 
       ["Land", "Land", "Sea", "Sea"],
       ["Sea", "Sea", "Land", "Sea"],
       ["Sea", "Sea", "Land", "Sea"]]

MAP1b = [[TypeTerritory.SEA, TypeTerritory.LAND, TypeTerritory.SEA, TypeTerritory.LAND],
         [TypeTerritory.LAND, TypeTerritory.LAND, TypeTerritory.SEA, TypeTerritory.SEA],
         [TypeTerritory.SEA, TypeTerritory.SEA, TypeTerritory.LAND, TypeTerritory.SEA],
         [TypeTerritory.SEA, TypeTerritory.SEA, TypeTerritory.LAND, TypeTerritory.SEA]]

MAP2 = [["Sea", "Sea"],
        ["Sea", "Sea"]]
MAP2b = [[TypeTerritory.SEA, TypeTerritory.SEA],
         [TypeTerritory.SEA, TypeTerritory.SEA]]

MAP3 = [["Land", "Land"],
        ["Land", "Land"]]
MAP3b = [[TypeTerritory.LAND, TypeTerritory.LAND],
         [TypeTerritory.LAND, TypeTerritory.LAND]]

MAP4 = [[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],# 0
        [1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],# 1
        [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],# 2
        [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],# 3
        [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],# 4
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],# 5
        [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0],# 6
        [0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0],# 7
        [0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],# 8
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],# 9
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],#10
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0],#11
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0],#12
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1],#13
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1],#14
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1]]#15

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
    
    def test_example_map(self):
        num_islands, new_map = count_islands_from_2d_map(MAP1b)
        self.assertEqual(num_islands, 3, "There are three islands!")
        print(new_map)
        
    def test_only_sea_map(self):
        num_islands, new_map = count_islands_from_2d_map(MAP2b)
        self.assertEqual(num_islands, 0, "There isn't any island!")
        
    def test_only_land_map(self):
        num_islands, new_map = count_islands_from_2d_map(MAP3b)
        self.assertEqual(num_islands, 1, "Maybe we are in a continent!")
        