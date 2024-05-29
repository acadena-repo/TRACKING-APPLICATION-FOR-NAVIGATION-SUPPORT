from abc import ABC, abstractmethod
import pygame
from pygame.math import Vector2


def load_animation():
    animation_images = []
    for i in range(7):
        image = pygame.image.load(f"./assets/target/{i}.png").convert_alpha()
        animation_images.append(image)
    return animation_images


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
        super().__init__(state, position)
        self.needle = pygame.image.load(
            "./assets/compass/0.png")
        self.angle = 0

    def render(self, surface):
        angle = self.orientation
        pinpoint = Vector2(390, 390)
        # Extract the needle in a surface
        needleTile = pygame.Surface((150, 150), pygame.SRCALPHA)
        needleTile.blit(self.needle, (0, 0))
        # Rotate image
        rotatedTile = pygame.transform.rotate(needleTile, angle)
        # shift location of the image
        pinpoint.x -= (rotatedTile.get_width() -
                       needleTile.get_width()) // 2
        pinpoint.y -= (rotatedTile.get_height() -
                       needleTile.get_height()) // 2
        surface.blit(rotatedTile, ((pinpoint.x), (pinpoint.y)))


class Target(Unit):
    def __init__(self, state, position):
        super().__init__(state, position)
        self.relative = Vector2(0, 0)
        self.frameIdx = 0
        self.refresh = 150
        self.timer = pygame.time.get_ticks()
        self.images = load_animation()
        self.target = self.images[self.frameIdx]

    def animate(self):
        self.target = self.images[self.frameIdx]
        if pygame.time.get_ticks() - self.timer > self.refresh:
            self.frameIdx += 1
            self.timer = pygame.time.get_ticks()

        if self.frameIdx >= len(self.images):
            self.frameIdx = 0

    def render(self, surface):
        # pygame.draw.circle(surface, (30, 144, 255), self.relative, 8)
        surface.blit(self.target, self.relative)


class Faceplate(Unit):
    def __init__(self, state, position):
        super().__init__(state, position)
        self.forklift = pygame.image.load(
            "./assets/forklift/0.png")
        self.rect = pygame.Rect(0, 0, 60, 60)

    def render(self, surface):
        spritePoint = Vector2(450, 450)
        # Extract the tile in a surface
        textureTile = pygame.Surface((60, 60), pygame.SRCALPHA)
        textureTile.blit(self.forklift, (0, 0), self.rect)
        rotatedTile = pygame.transform.rotate(textureTile, self.orientation)
        spritePoint.x -= (rotatedTile.get_width() -
                          textureTile.get_width()) // 2
        spritePoint.y -= (rotatedTile.get_height() -
                          textureTile.get_height()) // 2
        # Render the rotatedTile
        surface.blit(rotatedTile, (spritePoint.x - 15, spritePoint.y - 15))

        pygame.draw.circle(surface, (0, 0, 0), (465, 465), 45, 2)
        pygame.draw.circle(surface, (0, 0, 0), (465, 465), 130, 2)
        pygame.draw.circle(surface, (0, 0, 0), (465, 465), 260, 2)
        pygame.draw.circle(surface, (0, 0, 0), (465, 465), 390, 2)
