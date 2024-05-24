import os
from interfaces import UserInterface

os.environ['SDL_VIDEO_CENTERED'] = '1'


def main():
    UI = UserInterface()
    UI.run()


if __name__ == '__main__':
    main()
