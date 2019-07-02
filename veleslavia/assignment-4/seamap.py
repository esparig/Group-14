""" This module contains a function count_islands which counts islands
by recursively visiting connected land areas. That recursive algorithm
looping over the sea matrix and if we have a land, we should process
the corresponding island and add +1 to the total number of islands.
"""

from itertools import product
from typing import List
import unittest


def process_island(sea_map: List[List[bool]], visited: List[List[bool]], i: int, j: int):
    """
    Traverse an island and mark visited lands as 'visited'
    :param sea_map: original sea map
    :param visited: boolean map with visited tiles marked as True
    :param i: x coordinate of a tile in current island
    :param j: y coordinate of a tile in current island
    :return:
    """
    connected_directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    visited[i][j] = True
    for (move_i, move_j) in connected_directions:
        if 0 <= i+move_i < len(sea_map) and 0 <= j+move_j < len(sea_map[i+move_i]):
            if sea_map[i+move_i][j+move_j] and not visited[i+move_i][j+move_j]:
                process_island(sea_map, visited, i+move_i, j+move_j)
    return 1


def count_islands(sea_map: List[List[bool]]) -> int:
    """
    Count number of islands in the map.
    :param sea_map: 2D map of booleans where True represents LAND and False represents SEA
    :return: number of islands in the map
    """
    visited = [[False] * len(row) for row in sea_map]
    return sum(
        process_island(sea_map, visited, i, j)
        for (i, j) in product(range(len(sea_map)), range(len(sea_map[0])))
        if sea_map[i][j] and not visited[i][j])


class CountIslandsTest(unittest.TestCase):

    def test_count_islands(self):
        seamap = [[False, True, False, True],
                  [True, True, False, False],
                  [False, False, True, False],
                  [False, False, True, False]]
        self.assertEqual(count_islands(seamap), 3)
