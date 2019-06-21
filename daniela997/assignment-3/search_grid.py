def search_grid(grid, lexicon, position=(0, 0), prefix='', ):
    """
    Checks if words formed by moving along a grid are in a given lexicon of words.
    :param grid: Grid of characters to be traversed.
    :param lexicon: Lexicon which uses trie representation of words.
    :param position: Starting position in the grid.
    :param prefix: Prefix of word found so far.
    :return:
    """
    # Allowed directions to move along the grid - up, down, left, right and diagonals.
    allowed_directions = [
        (position[0] + 1, position[1]),
        (position[0] + 1, position[1] + 1),
        (position[0] + 1, position[1] - 1),
        (position[0] - 1, position[1]),
        (position[0] - 1, position[1] + 1),
        (position[0] - 1, position[1] - 1),
        (position[0], position[1] + 1),
        (position[0], position[1] - 1)
    ]
    # Move position in each possible direction
    for current_position in allowed_directions:
        # Check that move is allowed within grid and that chosen position has not been visited yet
        if len(grid) > current_position[0] >= 0 and len(grid[0]) > current_position[1] >= 0 \
                and grid[current_position[0]][current_position[1]] != '':
            # Check if prefix so far along with letter in current position is a prefix in the lexicon
            if lexicon.is_prefix(prefix + grid[current_position[0]][current_position[1]]):
                # Save prefix
                prefix = prefix + grid[current_position[0]][current_position[1]]
                # Mark position as visited
                grid[current_position[0]][current_position[1]] = ''
                # Recursively call with current position as starting position and new prefix
                yield from search_grid(grid, lexicon, current_position, prefix)
                # If prefix is a word in lexicon return it
                if lexicon.is_word(prefix):
                    yield prefix
