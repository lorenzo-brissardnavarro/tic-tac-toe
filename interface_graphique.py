import pygame
from pygame.locals import *
import pygame_gui

pygame.init()

dimension = 600
fenetre = pygame.display.set_mode((dimension, dimension))
pygame.display.set_caption("Tic Tac Toe")

def page_accueil():
    fond = pygame.image.load("background_morpion.png").convert()
    fond = pygame.transform.scale(fond, (dimension, dimension))

    play_icon = pygame.image.load("play_icon.png").convert_alpha()
    play_icon = pygame.transform.scale(play_icon, (40, 40))

    manager = pygame_gui.UIManager((dimension, dimension),theme_path="quick_start.json")


    titre = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(0, 40, dimension, 70),text="Jeu du Tic Tac Toe",manager=manager)
    titre.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR,params={"time_per_letter": 0.1})
 
    play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dimension/2)-125, dimension-160, 250, 80),text="JOUER",manager=manager,object_id="#play_button")

    clock = pygame.time.Clock()
    continuer = True

    while continuer:
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == play_button:
                    print("Tu as cliqué sur JOUER")

            manager.process_events(event)

        manager.update(time_delta)

        fenetre.blit(fond, (0, 0))
        manager.draw_ui(fenetre)
        btn_x, btn_y = play_button.rect.topleft
        icon_x = btn_x + 15
        icon_y = btn_y + 20

        fenetre.blit(play_icon, (icon_x, icon_y))

        pygame.display.flip()

    pygame.quit()


page_accueil()
