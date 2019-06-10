def search_grid(grid, lexicon, position=(0, 0), prefix='', ):
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
    for current_position in allowed_directions:
        if len(grid) > current_position[0] >= 0 and len(grid[0]) > current_position[1] >= 0 \
                and grid[current_position[0]][current_position[1]] != '':
            if lexicon.is_prefix(prefix + grid[current_position[0]][current_position[1]]):
                prefix = prefix + grid[current_position[0]][current_position[1]]
                grid[current_position[0]][current_position[1]] = ''
                yield from search_grid(grid, lexicon, current_position, prefix)
                if lexicon.is_word(prefix):
                    yield prefix
