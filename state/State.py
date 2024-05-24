from pygame.math import Vector2
from .Settings import Settings
from units import Compass


class State:
    def __init__(self):
        self.config = Settings()
        self.compass = Compass(self, Vector2(390, 390))
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

    def get_target(self):
        return self.targets[0]

    def add_target(self, target):
        self.targets.append(target)

    def remove_target(self):
        self.targets.clear()
