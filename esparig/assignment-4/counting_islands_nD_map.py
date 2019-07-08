"""
Assignment 4: Counting Islands.
[Optional assignment]: Given a n-dimensional representation of a map, compute the number of islands in the map.
"""
from typing import Tuple, List, DefaultDict
from terrain import Terrain


def count_islands_nD_map(map: DefaultDict) -> Tuple[int, List[List[int]]]:
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
        if map[territory].type == Terrain.LAND and not visited[territory]:
            stack = []
            stack.append(territory)
            visited[territory] = True
            while stack:
                current = stack.pop()
                island.append(current)
                for adjacent in map[current].adjacents:
                    if map[adjacent].type == Terrain.LAND and not visited[adjacent]:
                        stack.append(adjacent)
                        visited[adjacent] = True
        if island:
            list_islands.append(island)

    return len(list_islands), list_islands
