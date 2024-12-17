from __future__ import annotations
from typing import TYPE_CHECKING
import pygame
from tkinterSachen.qrcode_in_einem_tkinter_infobox_anzeigen import generate_qr_code

if TYPE_CHECKING:
    from PIL import Image
    from pygame import Surface


def generate_pygame_image(img: Image) -> Surface:

    # Konvertiere das PIL-Image in ein Pygame-Surface
    img = img.convert("RGBA")
    mode = img.mode
    size = img.size
    data = img.tobytes()
    pygame_img = pygame.image.fromstring(data, size, mode)
    return pygame_img


def display_qr_code(img: Image) -> None:
    """Zeigt das QR-Code-Bild in einem Pygame-Fenster an.

    Args:
        img (pygame.Surface): Das QR-Code-Bild als Pygame-Surface.
    """

    pygame.init()
    # Es gibt zwei Moeglichkeiten, die groesse des QR-Codes abzufragen
    #   x, y = img.size => vom PIL-Image
    #   x, y = pygame_img.get_size() => vom PyGame-Image
    print(f"{img.size =}")
    screen = pygame.display.set_mode(img.size)
    pygame.display.set_caption("QR-Code")

    pygame_img = generate_pygame_image(img)
    print(f"{pygame_img.get_size() =}")

    screen.blit(pygame_img, (0, 0))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    url = "https://www.example.com"
    pil_img = generate_qr_code(url)
    display_qr_code(pil_img)
