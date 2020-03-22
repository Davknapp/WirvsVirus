# -*- coding: UTF-8 -*-



# Pygame-Modul importieren.

import pygame
import random


# Import classes

from classes.human import human
from classes.player import player
from classes.gui import activeGui, UInterface
from img_lib import get_image,  background
from classes.model import Model
from classes.game_state import initGameState


# Überprüfen, ob die optionalen Text- und Sound-Module geladen werden konnten.

if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')

if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden!')

random.seed()

N_humans = 50
radius = 10
speed = 5

def main():

    # Initialisieren aller Pygame-Module und
    # Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).
    pygame.init()
    # Das Hauptfenster
    screen = pygame.display.set_mode((800, 800))
    screen.fill((0, 0, 0))
    # Surface auf der das Game lauft
    game_screen = pygame.Surface((800, 600))
    game_screen.fill((0, 0, 0))
    # Surface auf der die GUI lebt
    gui_screen = pygame.Surface((800, 200))
    gui_screen.fill((255, 255, 255))

    back = background('map.png', [0,0])

    # Init. GUI
    gui = UInterface(gui_screen)

    # Init. game state
    model = Model()
    gameState = initGameState(game_screen, model)
    me = gameState.the_player

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
        # Zeichne GUI und Game Surface
        screen.blit(gui_screen, (0, 0))
        screen.blit(game_screen, (0, 200))
        game_screen.blit(back.image,back.rect)

        # Update the game state
        gameState.frame_update()

        # Alle aufgelaufenen Events holen und abarbeiten.
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

        gameState.frame_render(game_screen)
        activeGui.render(game_screen)

        pygame.display.update()
        # Inhalt von screen anzeigen.
        pygame.display.flip()

# Überprüfen, ob dieses Modul als Programm läuft und nicht in einem anderen Modul importiert wird.
if __name__ == '__main__':
    # Unsere Main-Funktion aufrufen.
    main()
