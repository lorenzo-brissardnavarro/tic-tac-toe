import pygame
from pygame.locals import *
import pygame_gui

pygame.init()

dimension = 600
fenetre = pygame.display.set_mode((dimension, dimension))
pygame.display.set_caption("Tic Tac Toe")

manager = pygame_gui.UIManager((dimension, dimension),theme_path="quick_start.json")

def page_accueil():
    manager.clear_and_reset()
    fond = pygame.image.load("background_morpion.png").convert()
    fond = pygame.transform.scale(fond, (dimension, dimension))

    play_icon = pygame.image.load("play_icon.png").convert_alpha()
    play_icon = pygame.transform.scale(play_icon, (60, 60))

    titre = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(0, 40, dimension, 70),text="Jeu du Tic Tac Toe",manager=manager)
    titre.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR,params={"time_per_letter": 0.1})
 
    play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dimension/2)-125, dimension-120, 250, 80),text="JOUER",manager=manager)

    clock = pygame.time.Clock()
    continuer = True

    while continuer:
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == play_button:
                    page_choix()

            manager.process_events(event)

        manager.update(time_delta)

        fenetre.blit(fond, (0, 0))
        manager.draw_ui(fenetre)
        btn_x, btn_y = play_button.rect.topleft
        icon_x = btn_x + 15
        icon_y = btn_y + 10

        fenetre.blit(play_icon, (icon_x, icon_y))

        pygame.display.flip()


def page_choix():
    manager.clear_and_reset()
    fenetre.fill((0, 0, 0))

    label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(0, 40, 600, 50), text="Choisissez votre mode de jeu", manager=manager)

    image_mode1 = pygame.image.load("joueur_vs_joueur.png").convert_alpha()
    image_mode2 = pygame.image.load("joueur_vs_ia.png").convert_alpha()

    image_mode1 = pygame.transform.scale(image_mode1, (250, 350))
    image_mode2 = pygame.transform.scale(image_mode2, (250, 350))

    bouton_mode1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(35, 150, 250, 350),text="",manager=manager, object_id="#bouton_mode1")
    bouton_mode2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(315, 150, 250, 350),text="",manager=manager, object_id="#bouton_mode2")

    clock = pygame.time.Clock()
    continuer = True

    while continuer:
        time_delta = clock.tick(60)/1000.0

        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == bouton_mode1:
                    print("Mode 1 sélectionné")
                elif event.ui_element == bouton_mode2:
                    print("Mode 2 sélectionné")

            manager.process_events(event)

        manager.update(time_delta)

        fenetre.fill((0, 0, 0)) 
        manager.draw_ui(fenetre)

        fenetre.blit(image_mode1, (35, 150))
        fenetre.blit(image_mode2, (315, 150))

        pygame.display.flip()

page_accueil()
pygame.quit()
