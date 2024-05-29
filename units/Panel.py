import pygame

DISPLAY = (0, 64, 128)
BACKGROUND = (255, 255, 255)


class DisplayInfo(pygame.sprite.Sprite):
    def __init__(self, LocX, LocY, distance, least_angle, side):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("./assets/font/FiraSans-Regular.ttf", 28)
        if distance == -999:
            message = "***** Target Not Tracked *****"
        else:
            message = f"Distance to Target: {distance}   [m]     |     Rotage to {side}: {least_angle}  [Deg]"

        self.image = self.font.render(message, True, DISPLAY, BACKGROUND)
        self.rect = self.image.get_rect()
        self.rect.center = (LocX + self.image.get_width()//2,
                            LocY + self.image.get_height()//2)

    def update(self):
        self.kill()
