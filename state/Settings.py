from collections import namedtuple
from pygame.math import Vector2

constants = {
    'scan': 8,
    'meter2pixels': 10,
    'tileSize': Vector2(30, 30),
    'displayArea': Vector2(30, 30),
}

Structure = namedtuple('Settings', [
    'scan',
    'meter2pizels',
    'tileSize',
    'displayArea'
])


def Settings():
    return Structure(**constants)
