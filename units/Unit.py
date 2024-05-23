import math
from abc import ABC, abstractmethod
import pygame
from pygame.math import Vector2


class Unit(ABC):
    def __init__(self, state, position):
        self.state = state
        self.status = "visible"
        self.position = position
        self.orientation = 0

    @abstractmethod
    def render(self, surface):
        ...


class Compass(Unit):
    def __init__(self, state, position):
        super.__init__(state, position)
        self.needle = pygame.image.load(
            "./assets/compass/0.png").convert_alpha()
        self.pinpoint = Vector2(390, 390)
        self.azimuth = 0

    def render(self, surface):
        angle = self.azimuth
        # Extract the needle in a surface
        needleTile = pygame.Surface((150, 150), pygame.SRCALPHA)
        needleTile.blit(self.needle, (0, 0))
        # Rotate image
        rotatedTile = pygame.transform.rotate(needleTile, angle)
        # shift location of the image
        self.pinpoint.x -= (rotatedTile.get_width() -
                            needleTile.get_width()) // 2
        self.pinpoint.y -= (rotatedTile.get_height() -
                            needleTile.get_height()) // 2

        surface.blit(rotatedTile, ((self.pinpoint.x), (self.pinpoint.y)))

    def get_azimuth(self, target):
        distance = target - self.position
        angle = math.atan2(-distance.x, -distance.y) * 180 / math.pi
        self.azimuth = angle - self.orientation


class Target(Unit):
    def __init__(self, state, position):
        super.__init__(state, position)

    def render(self, surface):
        pygame.draw.circle(surface, (30, 144, 255),
                           (self.position.x - 15, self.position.y - 15), 8)
