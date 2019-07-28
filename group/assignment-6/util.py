from itertools import islice


# Utility sliding window function used to print moves
def window(seq, window_size=2):
    """Returns a sliding window over data iterable"""
    it = iter(seq)
    result = tuple(islice(it, window_size))
    if len(result) == window_size:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result
