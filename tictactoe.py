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

def est_remplie(grille):
    for ligne in grille:
        for element in ligne:
            if element == '-':
                return False
    return True

def victoire(grille):
    for k in range(3):
        if grille[k][0] != '-' and grille[k][0] == grille[k][1] == grille[k][2]:
            print("Aligenement horizontal")
            return True
        if grille[0][k] != '-' and grille[0][k] == grille[1][k] == grille[2][k]:
            print("Aligenement vertical")
            return True
    if grille[0][0] != '-' and grille[0][0] == grille[1][1] == grille[2][2]:
        print("Alignement diagonale haut bas")
        return True
    if grille[0][2] != '-' and grille[0][2] == grille[1][1] == grille[2][0]:
        print("Alignement diagonale bas haut")
        return True
    return False





