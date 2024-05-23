import pygame
from pygame.math import Vector2
from .Settings import Settings
from units import Compass


class State:
    def __init__(self):
        self.config = Settings()
        self.compass = Compass(self, Vector2(0, 0))
        self.targets = []

    @property
    def displayWidth(self):
        return int(self.config.displayArea.x)

    @property
    def displayHeight(self):
        return int(self.config.displayArea.y)

    @property
    def tileWidth(self):
        return int(self.config.tileSize.x)

    @property
    def tileHeight(self):
        return int(self.config.tileSize.y)

    @property
    def windowWidth(self):
        return int(self.config.displayArea.x * self.config.tileSize.x)

    @property
    def windowHeight(self):
        return int(self.config.displayArea.y * self.config.tileSize.y)
