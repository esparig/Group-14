from map_enum import Map


def multidimensional_indeces(start, stop, dimensions):
    """
    Generator that lists all index tuples for a ndarray
    :param start: origin for each vector
    :param stop: length of each vector (dimension)
    :param dimensions: number of dimensions
    :return:
    """
    if not dimensions:
        yield []
        return
    for outer in multidimensional_indeces(start, stop, dimensions - 1):
        for inner in range(start, stop):
            yield outer + [inner, ]


def get_allowed_directions(position):
    """
    Generates a list of allowed directions from current position.
    Assuming we can make a step in one direction at a time
    - no diagonal steps
    :param position:
    :return:
    """
    allowed_directions = []

    for dimension in range(len(position)):
        step_forward = list.copy(position)
        step_forward[dimension] = step_forward[dimension] + 1
        step_back = list.copy(position)
        step_back[dimension] = step_back[dimension] - 1
        allowed_directions.append(step_forward)
        allowed_directions.append(step_back)

    return allowed_directions


def walk_land(grid, position):
    allowed_directions = get_allowed_directions(position)
    try:
        # I can't work out how to get a reference
        # to array item in an ndarray
        if grid[position[0]][position[1]] != Map.SEA:
            grid[position[0]][position[1]] = Map.SEA
            for direction in allowed_directions:
                walk_land(grid, position + direction)
        return
    except IndexError:
        return


def count_islands(grid, dimensions=2):
    if len(grid) == 0:
        return 0

    islands_count = 0
    for island_index in list(multidimensional_indeces(0, dimensions, dimensions)):
        # Select array item using tuple island_index to index in n dimensions
        island = grid
        for i in island_index:
            island = island[i]
        if island == Map.LAND:
            islands_count += 1
            walk_land(grid, island_index)

    return islands_count

