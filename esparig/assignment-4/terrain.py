"""
Terrain definitions.
A map is composed by n terrains.
"""
from enum import Enum

class Terrain(Enum):
    """Enum to define types of terrains in a map. Useful to:
    - avoid typing errors,
    - better memory usage.
    """
    SEA = 0
    LAND = 1