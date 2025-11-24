import random


def creation_grille():
    grille = []
    for i in range(3):
        grille.append(['-'] * 3)
    return grille

def est_remplie(grille):
    for ligne in grille:
        for element in ligne:
            if element == '-':
                return False
    return True

def victoire(grille, joueur):
    for k in range(3):
        if grille[k][0] == grille[k][1] == grille[k][2] == joueur:
            return True
        if  grille[0][k] == grille[1][k] == grille[2][k] == joueur:
            return True
    if grille[0][0] == grille[1][1] == grille[2][2] == joueur:
        return True
    if grille[0][2] == grille[1][1] == grille[2][0] == joueur:
        return True
    return False

def changement_joueur(joueur):
    if joueur == 'X':
        return "O"
    else:
        return "X"

def coup_gagnant(grille, symbole):
    for i in range(3):
        for j in range(3):
            if grille[i][j] == "-":
                grille[i][j] = symbole
                if victoire(grille, symbole):
                    grille[i][j] = "O"
                    return grille, True
                grille[i][j] = "-"
    return grille, False

def positionnement_ordi(grille):
    cases_vides = []
    for i in range(3):
        for j in range(3):
            if grille[i][j] == "-":
                cases_vides.append((i, j))
    h, v = random.choice(cases_vides)
    grille[h][v] = "O"
    return grille

def tour_ordi(grille):
    nouvelle_grille, gagne = coup_gagnant(grille, "O")
    if gagne:
        return nouvelle_grille
    nouvelle_grille, bloque = coup_gagnant(grille, "X")
    if bloque:
        return nouvelle_grille
    return positionnement_ordi(grille)

        
        



        


