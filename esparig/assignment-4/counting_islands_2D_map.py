"""
Assignment 4: Counting Islands.
Given a 2-dimensional map of square tiles, compute the number of islands in the map.
"""
from typing import Tuple, List, DefaultDict
from terrain import Terrain


def count_islands_2D_map(map: List[List[str]]) -> int:
    """Given a two-dimensional map, indicating Land or Sea terrain for each cell, 
    this function returns the number of found islands and a representation identifying them.
    """
    width, height = len(map), len(map[0])
    visited = [[False]*width for _  in range(height)]
    
    def explore_island(i: int, j: int):
        """Explore the adjacent Land cells using DFS
        """
        if i >= 0 and i < width and j >= 0 and j < height:
            if not visited[i][j] and map[i][j] == Terrain.LAND:
                visited[i][j] = True
                for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    explore_island(i+x, j+y)
    
    num_islands = 0
    for i in range(width):
        for j in range(height):
            if not visited[i][j] and map[i][j] == Terrain.LAND:
                    num_islands += 1
                    explore_island(i, j)
                
    return num_islands
