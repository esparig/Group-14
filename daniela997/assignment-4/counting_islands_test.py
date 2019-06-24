import unittest
from map_enum import Map
from counting_islands import count_islands, walk_land


class CountingIslandsTest(unittest.TestCase):
    def test_walk_land_return(self):
        world_grid = [[Map.SEA, Map.LAND, Map.SEA],
                      [Map.SEA, Map.LAND, Map.SEA],
                      [Map.SEA, Map.LAND, Map.SEA]]
        result = walk_land(world_grid, [1, 1])
        self.assertEqual(result, 0)
        # Index out of bound
        result = walk_land(world_grid, [1, 5])
        self.assertEqual(result, 1)

    def test_walk_land_mark(self):
        world_grid = [[Map.SEA, Map.LAND, Map.SEA],
                      [Map.SEA, Map.LAND, Map.SEA],
                      [Map.SEA, Map.LAND, Map.SEA]]
        ocean = [[Map.SEA, Map.SEA, Map.SEA],
                 [Map.SEA, Map.SEA, Map.SEA],
                 [Map.SEA, Map.SEA, Map.SEA]]
        # Sink all LAND cells
        walk_land(world_grid, [1, 1])
        self.assertEqual(world_grid, ocean)

    def test_count_islands(self):
        world_grid = [[Map.SEA, Map.LAND, Map.SEA, Map.LAND],
                      [Map.LAND, Map.LAND, Map.SEA, Map.SEA],
                      [Map.SEA, Map.SEA, Map.LAND, Map.SEA],
                      [Map.SEA, Map.SEA, Map.LAND, Map.SEA]]
        islands_count = count_islands(world_grid)
        self.assertEqual(islands_count, 3)

        ocean = [[Map.SEA, Map.SEA, Map.SEA],
                 [Map.SEA, Map.SEA, Map.SEA],
                 [Map.SEA, Map.SEA, Map.SEA]]
        islands_count = count_islands(ocean)
        self.assertEqual(islands_count, 0)

        continent = [[Map.LAND, Map.LAND, Map.LAND],
                    [Map.LAND, Map.LAND, Map.LAND]]
        islands_count = count_islands(continent)
        self.assertEqual(islands_count, 1)


if __name__ == '__main__':
    unittest.main()
