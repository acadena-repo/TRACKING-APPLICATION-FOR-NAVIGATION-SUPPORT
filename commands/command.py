from abc import ABC, abstractmethod
from pygame.math import Vector2
import math
from units import DisplayInfo


def tracking_information(reference, target, angle, orientation):
    distance = round(reference.distance_to(target)/10, 0)
    side = ["Left", "Right"]
    least_angle = angle - orientation
    if least_angle > 0:
        return distance, abs(int(least_angle)), side[0]
    elif least_angle < 0:
        return distance, abs(int(least_angle)), side[1]

    return distance, abs(int(least_angle)), "None"


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
        self.state.panel.update()
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
            tracking = tracking_information(
                compass.position, self.target.position, angle, self.displacement['orientation'])
            self.state.panel.add(DisplayInfo(
                70, 5, tracking[0], tracking[1], tracking[2]))
        else:
            self.state.panel.add(DisplayInfo(275, 5, -999, 0.0, "None"))
