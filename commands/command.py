from abc import ABC, abstractmethod
from pygame.math import Vector2
import math


class Command(ABC):
    @abstractmethod
    def update(self):
        ...


class NeedleCommand(Command):
    def __init__(self, state, displacement, target=None):
        self.state = state
        self.displacement = displacement
        self.target = target

    def update(self):
        compass = self.state.compass
        compass.orientation = self.displacement['orientation']
        compass.position.x = self.displacement['x']
        compass.position.y = self.displacement['y']

        if self.target:
            difference = compass.position - self.target.position
            targetTile = Vector2(465, 465)
            targetTile.x -= difference.x
            targetTile.y -= difference.y
            self.target.relative.x = targetTile.x
            self.target.relative.y = targetTile.y
            reference = Vector2(465, 465) - targetTile
            angle = math.atan2(reference.x, reference.y) * 180 / math.pi
            compass.orientation = angle
            print(
                compass.position, self.displacement['orientation'], self.target.position, targetTile, difference)
