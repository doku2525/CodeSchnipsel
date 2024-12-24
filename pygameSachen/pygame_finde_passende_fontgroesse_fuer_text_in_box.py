import pygame
from pygame.locals import *
import sys
from unittest import TestCase
# import testen.einfache_tests_in_datei as tmsg


SCREEN_SIZE = (400, 300)


def main():
    test = TestCase()
    font_name = 'Stift.ttf'
    test_string = "0:00:00"

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('display')
    font = pygame.font.Font(font_name, 100)
    sys_font = pygame.font.SysFont(None, 100)

    text_mit_font = font.render(test_string, True, (0, 0, 0))
    text_mit_sys_font = sys_font.render(test_string, True, (0, 0, 0))

    while True:
        screen.fill((255, 255, 255))
        screen.blit(text_mit_font, (0, 0))
        screen.blit(text_mit_sys_font, (10, 100))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()
