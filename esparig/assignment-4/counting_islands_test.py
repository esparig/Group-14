"""Unit tests for Assignment 4: Counting Islands"""
from collections import namedtuple, defaultdict
import unittest
from terrain import Terrain
from counting_islands_2D_map import count_islands_2D_map
from counting_islands_nD_map import count_islands_nD_map



MAP_4_x_4 = [[Terrain.SEA, Terrain.LAND, Terrain.SEA, Terrain.LAND],
             [Terrain.LAND, Terrain.LAND, Terrain.SEA, Terrain.SEA],
             [Terrain.SEA, Terrain.SEA, Terrain.LAND, Terrain.SEA],
             [Terrain.SEA, Terrain.SEA, Terrain.LAND, Terrain.SEA]]

MAP_ONLY_SEA = [[Terrain.SEA, Terrain.SEA],
        [Terrain.SEA, Terrain.SEA]]

MAP_ONLY_LAND = [[Terrain.LAND, Terrain.LAND],
        [Terrain.LAND, Terrain.LAND]]

TERRITORY = namedtuple('TERRITORY', ['type', 'adjacents'])
TERRITORIES = []

TERRITORIES.append(TERRITORY(type=Terrain.SEA,  adjacents=[1, 2, 3]))
TERRITORIES.append(TERRITORY(type=Terrain.LAND, adjacents=[0, 3, 4, 6]))
TERRITORIES.append(TERRITORY(type=Terrain.LAND, adjacents=[0, 3, 5, 7]))
TERRITORIES.append(TERRITORY(type=Terrain.SEA,  adjacents=[0, 1, 2, 6, 7, 8]))

TERRITORIES.append(TERRITORY(type=Terrain.SEA,  adjacents=[1, 6, 9, 11]))
TERRITORIES.append(TERRITORY(type=Terrain.LAND, adjacents=[2, 7, 10, 12]))
TERRITORIES.append(TERRITORY(type=Terrain.SEA,  adjacents=[1, 3, 4, 8, 11, 13]))
TERRITORIES.append(TERRITORY(type=Terrain.SEA,  adjacents=[2, 3, 5, 8, 12, 14]))

TERRITORIES.append(TERRITORY(type=Terrain.LAND, adjacents=[3, 6, 7, 13, 14, 15]))
TERRITORIES.append(TERRITORY(type=Terrain.LAND, adjacents=[4, 11]))
TERRITORIES.append(TERRITORY(type=Terrain.SEA, adjacents=[5, 12]))
TERRITORIES.append(TERRITORY(type=Terrain.SEA, adjacents=[4, 6, 9, 13]))

TERRITORIES.append(TERRITORY(type=Terrain.LAND, adjacents=[5, 7, 10, 14]))
TERRITORIES.append(TERRITORY(type=Terrain.LAND, adjacents=[6, 8, 11, 15]))
TERRITORIES.append(TERRITORY(type=Terrain.SEA,  adjacents=[7, 8, 12, 15]))
TERRITORIES.append(TERRITORY(type=Terrain.LAND, adjacents=[8, 13, 14]))

MAP_GRAPH = defaultdict(tuple)

for idx, terr in enumerate(TERRITORIES):
    MAP_GRAPH[idx] = terr

class TestCountingIslands(unittest.TestCase):
    """Assuming the map is well provided, we test the output of the count_islands function.
    """
    def test_example_map(self):
        """Test a 2D map where each cell represents a type of territory (Sea or Land).
        """
        num_islands = count_islands_2D_map(MAP_4_x_4)
        self.assertEqual(num_islands, 3, "There are three islands!")
        
    def test_only_sea_map(self):
        """Test a 2D map containing only Sea
        """
        num_islands = count_islands_2D_map(MAP_ONLY_SEA)
        self.assertEqual(num_islands, 0, "There isn't any island!")
        
    def test_only_land_map(self):
        """Test a 2D map containing only Land
        """
        num_islands = count_islands_2D_map(MAP_ONLY_LAND)
        self.assertEqual(num_islands, 1, "Maybe we are in a continent!")
    
    def test_graph_map(self):
        """Test a nD map built from an adjacency list
        """
        num_islands, list_islands = count_islands_nD_map(MAP_GRAPH)
        self.assertEqual(num_islands, 4)
        self.assertEqual(list_islands, [[1], [2, 5, 12], [8, 15, 13], [9]])
