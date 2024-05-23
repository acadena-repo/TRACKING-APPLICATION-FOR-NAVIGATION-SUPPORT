from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def update(self):
        ...


class NeedleCommand(Command):
    def __init__(self, state, compass, displacement, target=None):
        self.state = state
        self.compass = compass
        self.displacement = displacement
        self.target = target

    def update(self):
        self.compass.position.x = self.displacement['x']
        self.compass.position.y = self.displacement['y']
        self.compass.orientation = self.displacement['orientation']

        if self.target:
            self.compass.get_azimuth(self.target)
