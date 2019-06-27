"""
Assignment 4: Counting Islands.
Given a 2-dimensional map of square tiles, compute the number of islands in the map.
Optional: The map is a n-Dimensional representation.
"""
from enum import Enum
from typing import Tuple, List, DefaultDict

def count_islands(map: List[List[str]]) -> int:
    """Given a two-dimensional map, indicating Land or Sea terrain for each cell, 
    this function returns the number of found islands and a representation identifying them.
    """
    width, height = len(map), len(map[0])
    visited = [[None]*width for _  in range(height)]
    
    def explore_island(i: int, j: int, id_island: int) -> Tuple[int, List[List[int]]]:
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

def count_islands_from_graph_map(map: DefaultDict) -> Tuple[int, List[List[int]]]:
    """Given a map as a dictionary where:
    key = id of the terrain 
    value = named tuple with type of territory and list of adjacent territories
    
    Using iterative DFS:
    
    Returns: number of islands and list of islands (as a list of territories)
    """
    
    visited = [False]*len(map)
    
    list_islands = []
    for territory in range(len(map)):
        island = []
        if map[territory].type == "Land" and not visited[territory]:
            stack = []
            stack.append(territory)
            visited[territory] = True
            while stack:
                current = stack.pop()
                island.append(current)
                for adjacent in map[current].adjacents:
                    if map[adjacent].type == "Land" and not visited[adjacent]:
                        stack.append(adjacent)
                        visited[adjacent] = True
        if island:
            list_islands.append(island)
    return len(list_islands), list_islands
