# -*- coding: UTF-8 -*-



# Pygame-Modul importieren.

import pygame
import random
import numpy as np



# Überprüfen, ob die optionalen Text- und Sound-Module geladen werden konnten.

if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')

if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden!')

random.seed()

class human(object):
    #define position of the human,  and the current movement.
    #draw a cricle representing the human.
    def __init__(self, limit_x, limit_y,  screen):
        self.posx = random.randint(0,limit_x)
        self.posy = random.randint(0,limit_y)
        alpha = random.randint(0,359)
        self.movx = int(np.cos(alpha)*10)
        self.movy = int(np.sin(alpha)*10)
        pygame.draw.circle(screen, (255,255,255), (self.posx, self.posy), 10)

    def movement(self, screen):
        self.posx += self.movx
        self.posy += self.movy
        pygame.draw.circle(screen, (255,255,255), (self.posx, self.posy), 10)


class player(object):
    def __init__(self, screen):
        self.posx = 400
        self.posy = 300
        pygame.draw.circle(screen, (255,0,0), (self.posx, self.posy), 10)

    def handle_input(self, key):
        # Linke Pfeiltaste wird gedrückt:
        if key == pygame.K_LEFT:
            # x-Position der Spielfigur anpassen,
            self.posx -= 1
        # Und nochmal für die rechte Pfeiltaste.
        if key == pygame.K_RIGHT:
            self.posx += 1
        if key == pygame.K_UP:
            self.posy -= 1
        if key == pygame.K_DOWN:
            self.posy += 1

    def render(self, screen):
        pygame.draw.circle(screen, (255,0,0), (self.posx, self.posy), 10)





def main():

    # Initialisieren aller Pygame-Module und
    # Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    screen.fill((0, 0, 0))
    human_list = [human(800,600,screen) for i in range(10)]
    me = player(screen)

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

        for person in human_list:
            person.movement(screen)


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
