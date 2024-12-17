import pygame
import qrcode
from tkinterSachen.qrcode_in_einem_tkinter_infobox_anzeigen import generate_qr_code


def generate_pygame_image(img):

    # Konvertiere das PIL-Image in ein Pygame-Surface
    img = img.convert("RGBA")
    mode = img.mode
    size = img.size
    data = img.tobytes()
    pygame_img = pygame.image.fromstring(data, size, mode)
    return pygame_img


def display_qr_code(img):
    """Zeigt das QR-Code-Bild in einem Pygame-Fenster an.

    Args:
        img (pygame.Surface): Das QR-Code-Bild als Pygame-Surface.
    """

    pygame.init()
    screen = pygame.display.set_mode(img.size)   # (320,320)
    pygame.display.set_caption("QR-Code")

    pygame_img = generate_pygame_image(img)
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

