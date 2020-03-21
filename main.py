# -*- coding: UTF-8 -*-



# Pygame-Modul importieren.

import pygame
import random
import numpy as np


# Import classes

from classes.human import human
from classes.player import player
from img_lib import get_image

# Überprüfen, ob die optionalen Text- und Sound-Module geladen werden konnten.

if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')

if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden!')

random.seed()

N_humans = 100
radius = 10
speed = 5

def main():

    # Initialisieren aller Pygame-Module und
    # Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.fill((0, 0, 0))
    # Init. humans

    img = pygame.transform.scale(get_image('healthy.png'), (20, 20))
    humans = [human(id, screen, img,  r=radius, v=speed) for id in range(N_humans)]
    humans[0].infection()
    me_img = pygame.transform.scale(get_image('myself.png'), (20, 20))
    me = player(screen,  me_img)


    # Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendrücke wiederholt senden.

    pygame.display.set_caption("Virus-Simulation")

    pygame.mouse.set_visible(1)

    pygame.key.set_repeat(1, 30)


    pygame.display.update()

    # Clock-Objekt erstellen, das wir benötigen, um die Framerate zu begrenzen.
    clock = pygame.time.Clock()
    # Die Schleife, und damit unser Spiel, läuft solange running == True.
    running = True
    while running:
        # Framerate auf 30 Frames pro Sekunde beschränken.
        # Pygame wartet, falls das Programm schneller läuft.
        clock.tick(30)
        # screen-Surface mit Schwarz (RGB = 0, 0, 0) füllen.
        screen.fill((0,0,0))
        # Alle aufgelaufenen Events holen und abarbeiten.

        for id, person in enumerate(humans):
            # humans_positions[id,0] = person.posx
            # humans_positions[id,1] = person.posy
            # normalize = True -> Geschwindigkeit ist konstant
            # normalize = False -> Geschwindigkeit ist "physikalisch"
            person.collisions(humans, normalize=True)
            person.check_state()
            person.movement()
            person.render(screen)

        for event in pygame.event.get():
            # Spiel beenden, wenn wir ein QUIT-Event finden.
            if event.type == pygame.QUIT:
                running = False
            # Wir interessieren uns auch für "Taste gedrückt"-Events.
            if event.type == pygame.KEYDOWN:
                me.handle_input(event.key)
                # Wenn Escape gedrückt wird, posten wir ein QUIT-Event in Pygames Event-Warteschlange.
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
        me.render(screen)
        pygame.display.update()
        # Inhalt von screen anzeigen.
        pygame.display.flip()

# Überprüfen, ob dieses Modul als Programm läuft und nicht in einem anderen Modul importiert wird.

if __name__ == '__main__':
    # Unsere Main-Funktion aufrufen.
    main()
