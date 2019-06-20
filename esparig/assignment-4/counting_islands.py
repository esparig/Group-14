"""
Assignment 4: Counting Islands.
Given a 2-dimensional map of square tiles, compute the number of islands in the map.
"""
from typing import List
from enum import Enum

class TypeTerritory:
    """Enum to define types of tiles. Useful to avoid typing errors.
    """
    SEA = 0
    LAND = 1

class Territory:
    """Node-like Data Structure for a territory. They will form the graph representation of a map.
    """
    def __init__(self, id: int, type: 'TypeTerritory', adjacents: List['Territory']):
        self.id = id
        self.type = type
        self.adjacents = adjacents

def count_islands_from_2d_map(map: List[List['TypeTerritory']]) -> int:
    """Given a two-dimensional map, indicating Land or Sea terrain for each cell, 
    this function returns the number of found islands and a representation identifying them.
    """
    width, height = len(map), len(map[0])
    visited = [[None]*width for _  in range(height)]
    
    def explore_island(i: int, j: int, id_island: int):
        """Explore the adjacent Land cells using DFS
        """
        if i >= 0 and i < width and j >= 0 and j < height:
            if not visited[i][j] and map[i][j] == TypeTerritory.LAND:
                visited[i][j] = id_island
                for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    explore_island(i+x, j+y, id_island)
    
    num_islands = 0
    for i in range(width):
        for j in range(height):
            if not visited[i][j]:
                if map[i][j] == TypeTerritory.LAND:
                    num_islands += 1
                    explore_island(i, j, num_islands)
                else:
                    visited[i][j] = 0
                
    return num_islands, visited

def count_islands(map: List[List[str]]) -> int:
    """Given a two-dimensional map, indicating Land or Sea terrain for each cell, 
    this function returns the number of found islands and a representation identifying them.
    """
    width, height = len(map), len(map[0])
    visited = [[None]*width for _  in range(height)]
    
    def explore_island(i: int, j: int, id_island: int):
        """Explore the adjacent Land cells using DFS
        """
        if i >= 0 and i < width and j >= 0 and j < height:
            if not visited[i][j] and map[i][j] == "Land":
                visited[i][j] = id_island
                for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    explore_island(i+x, j+y, id_island)
    
    num_islands = 0
    for i in range(width):
        for j in range(height):
            if not visited[i][j]:
                if map[i][j] == "Land":
                    num_islands += 1
                    explore_island(i, j, num_islands)
                else:
                    visited[i][j] = 0
                
    return num_islands, visited

def count_islands_from_graph_map(map):
    pass
