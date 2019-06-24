from map_enum import Map
from counting_islands import count_islands

import sys

def main(args):
    world_grid = [[Map.SEA, Map.LAND, Map.SEA, Map.LAND],
                  [Map.LAND, Map.LAND, Map.SEA, Map.SEA],
                  [Map.SEA, Map.SEA, Map.LAND, Map.SEA],
                  [Map.SEA, Map.SEA, Map.LAND, Map.SEA]]
    print("Number of islands in the grid is", count_islands(world_grid))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))