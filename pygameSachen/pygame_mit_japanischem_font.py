import pygame
from pygame.locals import *   # 定数QUITを使うため。importしない場合は、pygame.QUITとする。
import sys

""" Aus dem Internet kopiert
siehe: https://collatz.hatenablog.com/entry/2022/04/01/153316
"""
SCREEN_SIZE = (400, 300)

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)   # 画面の大きさを設定する
    pygame.display.set_caption('display')   # 画面のタイトルを設定する
    font = pygame.font.Font('Stift.ttf', 120)
    text = font.render('日本語', True, (0, 0, 0))

    while True:
        screen.fill((255, 255, 255))   # 画面を白く塗りつぶす
        screen.blit(text, (10, 10))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == '__main__':
    main()