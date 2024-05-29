import pygame
from pygame.math import Vector2
from state import State
from commands import NeedleCommand
from units import Target, Faceplate
from .sensor import Sensor


class UserInterface:
    def __init__(self):
        # initialization
        pygame.init()
        self.state = State()
        self.window = pygame.display.set_mode(
            (self.state.windowWidth, self.state.windowHeight))
        pygame.display.set_caption("FITS Navigation")
        pygame.display.set_icon(pygame.image.load("./assets/icon.ico"))
        self.faceplate = Faceplate(self.state, Vector2(450, 450))
        # Connect to sensor
        self.sensor = Sensor()
        # Controls
        self.tracking = False
        self.commands = []
        # Loop properties
        self.fps = self.state.config.scan
        # self.fps = 1
        self.clock = pygame.time.Clock()
        self.running = True

    def request(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_t:
                    new_position = Vector2(350, 470)
                    target = Target(self.state, new_position)
                    self.state.add_target(target)
                    self.tracking = True
                elif event.key == pygame.K_r:
                    self.state.remove_target()
                    self.tracking = False

        new_location = self.sensor.send("pose")
        self.faceplate.orientation = new_location['orientation']
        reference = self.state.get_target() if self.tracking else None
        self.commands.append(
            NeedleCommand(self.state, new_location, reference)
        )

    def update(self):
        for command in self.commands:
            command.update()
        self.commands.clear()
        if self.tracking:
            self.state.targets[0].animate()

    def render(self):
        self.window.fill((255, 255, 255))
        if self.tracking:
            self.state.targets[0].render(self.window)
        self.state.panel.draw(self.window)
        self.state.compass.render(self.window)
        self.faceplate.render(self.window)

        pygame.display.update()

    def run(self):
        while self.running:
            self.request()
            self.update()
            self.render()
            self.clock.tick(self.fps)
        pygame.quit()
