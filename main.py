# -*- coding: UTF-8 -*-



# Pygame-Modul importieren.

import pygame
import random
import numpy as np


# Import classes

from classes.human import human
from classes.player import player
from img_lib import get_image,  background
from classes.model import Model
from classes.game_state import initGameState
from classes.abstract_controller import AbstractController

# Überprüfen, ob die optionalen Text- und Sound-Module geladen werden konnten.

if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')

if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden!')

random.seed()

N_humans = 50
radius = 10
speed = 5

# Global State

from classes.app_instance import AppInstance

def main():

    # Initialisieren aller Pygame-Module und
    # Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.fill((0, 0, 0))

    back = background('map.png', [0,0])
    #screen.fill([255, 255, 255])
    # Init. game state
    model = Model()
    gameState = initGameState(screen, model)

    #   Set gameState as first controller to be run
    AppInstance.set_next_controller(gameState)

    # Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendrücke wiederholt senden.

    pygame.display.set_caption("Virus-Simulation")

    pygame.mouse.set_visible(1)

    pygame.key.set_repeat(1, 30)

    pygame.display.update()

    # Clock-Objekt erstellen, das wir benötigen, um die Framerate zu begrenzen.
    clock = pygame.time.Clock()
    # Die Schleife, und damit unser Spiel, läuft solange running == True.
    AppInstance.running = True
    
    while AppInstance.running:
        # Framerate auf 30 Frames pro Sekunde beschränken.
        # Pygame wartet, falls das Programm schneller läuft.
        clock.tick(30)
        # screen-Surface mit Schwarz (RGB = 0, 0, 0) füllen.
        #screen.fill((0,0,0))
        screen.blit(back.image,back.rect)

        # Update controller
        if AppInstance.next_controller is not None:
            if AppInstance.active_controller is not None:
                AppInstance.active_controller.finish()
            AppInstance.active_controller = AppInstance.next_controller
            AppInstance.next_controller = None
            AppInstance.active_controller.start()

        # Update the game state
        AppInstance.active_controller.frame_update()

        AppInstance.active_controller.frame_render(screen)

        pygame.display.update()
        # Inhalt von screen anzeigen.
        pygame.display.flip()

# Überprüfen, ob dieses Modul als Programm läuft und nicht in einem anderen Modul importiert wird.
if __name__ == '__main__':
    # Unsere Main-Funktion aufrufen.
    main()
