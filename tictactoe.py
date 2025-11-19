import random

joueurs = ["X", "O"]

def creation_grille():
    grille = []
    for i in range(3):
        grille.append(['-'] * 3)
    return grille

def affichage(grille):
    for ligne in grille:
        for element in ligne:
            print(element, end=' ')
        print()




