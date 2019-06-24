from map_enum import Map


def walk_land(grid, position):
    """
    Walks grid cells which are LAND - essentially depth
    first search.
    :param grid: Grid to traverse
    :param position: Current position
    :return: When all adjacent LAND cells are explored
    """

    # We can only move horizontally or diagonally from
    # current position
    allowed_directions = [
        (position[0] + 1, position[1]),
        (position[0] - 1, position[1]),
        (position[0], position[1] + 1),
        (position[0], position[1] - 1)
    ]

    try:
        # If current cell is not SEA, sink LAND cell
        # so we can't come back and then
        # walk neighbouring LAND cells
        if grid[position[0]][position[1]] != Map.SEA:
            grid[position[0]][position[1]] = Map.SEA
            for direction in allowed_directions:
                walk_land(grid, direction)
        return 0
    except IndexError:
        # Instead of manually checking indeces
        return 1


def count_islands(grid):
    """
    Grid to count the islands in. Assumed to be 2D array.
    :param grid:
    :return:
    """
    if len(grid) == 0:
        return 0

    islands_count = 0

    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == Map.LAND:
                islands_count += 1
                walk_land(grid, (row, column))

    return islands_count



