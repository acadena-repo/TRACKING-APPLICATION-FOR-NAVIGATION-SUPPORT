import pygame
from state import State
from commands import NeedleCommand
from units import Target
from sensor import Sensor


class UserInterface:
    def __init__(self):
        # initialization
        pygame.init()
        self.state = State()
        self.window = pygame.display.set_mode(
            (self.state.windowWidth, self.state.windowHeight))
        pygame.display.set_caption("FITS Navigation")
        pygame.display.set_icon(pygame.image.load("./assets/icon.ico"))

        # Controls
        self.commands = []
        # Loop properties
        self.fps = self.state.config.scan
        self.clock = pygame.time.Clock()
        self.run = True
