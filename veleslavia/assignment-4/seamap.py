from typing import List
import unittest


def process_island(sea_map: List[List[bool]], i: int, j: int):
    connected_directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    sea_map[i][j] = False
    for (move_i, move_j) in connected_directions:
        if 0 <= i+move_i < len(sea_map) and 0 <= j+move_j < len(sea_map[i+move_i]):
            if sea_map[i+move_i][j+move_j]:
                process_island(sea_map, i+move_i, j+move_j)


def count_islands(sea_map: List[List[bool]]) -> int:
    n_islands = 0
    for i in range(len(sea_map)):
        for j in range(len(sea_map[i])):
            # if land
            if sea_map[i][j]:
                n_islands += 1
                process_island(sea_map, i, j)
    return n_islands


class CountIslandsTest(unittest.TestCase):

    def test_count_islands(self):
        seamap = [[False, True, False, True],
                  [True, True, False, False],
                  [False, False, True, False],
                  [False, False, True, False]]
        self.assertEqual(count_islands(seamap), 3)
