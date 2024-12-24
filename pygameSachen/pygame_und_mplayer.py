import subprocess

import pygame

#video = '欢乐颂片尾曲MV《总有幸福在等你》五美合唱 [BV1Ks41167Gk].mp4'  # TODO Probleme bei Leerzeichen?
video = "musiktestvideo.mp4"
player = "mpv"
# befehl und Parameter werden einfach als Liste aus Strings uebergeben
mplayer_process = subprocess.Popen([player, video, "-loop", "0"])

pygame.init()
screen = pygame.display.set_mode((800, 600))


def send_mplayer_command(command):
    subprocess.call([player, command])

# TODO Reagiert ueberhaupt nicht auf Tastaturkommandos von pygame aus. K_q zum beenden funktioniert,
#   aber send_mplayer_command() liefert Fehlermeldung zum Beispiel:
#       Exiting... (Errors when loading file)
#       [file] Cannot open file 'seek -10': No such file or directory
#       Failed to open seek -10.

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_p:
                # Pause/Play mplayer
                send_mplayer_command("pause")
            elif event.key == pygame.K_LEFT:
                # 10 Sekunden zurückspulen
                send_mplayer_command("seek -10")
            elif event.key == pygame.K_DOWN:
                send_mplayer_command("seek -60")
            elif event.key == pygame.K_RIGHT:
                send_mplayer_command("seek 10")
            elif event.key == pygame.K_UP:
                send_mplayer_command("seek 60")
            elif event.key == pygame.K_s:
                send_mplayer_command("screenshot")
            elif event.key == pygame.K_i:
                send_mplayer_command("show-progress")

            # ... (weitere Tastaturkürzel)

            elif event.key == pygame.K_p and event.mod & pygame.KMOD_CTRL:
                # Benutzerdefinierte Aktion: value -= 1
                print("Taste mit CTRL gedrueckt")
                # ... (weitere benutzerdefinierte Aktionen)
    current_time = "get_current_time_from_mplayer()"
    font = pygame.font.Font(None, 36)
    text = font.render(str(current_time), True, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.flip()

mplayer_process.terminate()
pygame.quit()
