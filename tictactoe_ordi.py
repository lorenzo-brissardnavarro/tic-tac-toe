import random

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

def saisie_coordonnees(grille):
    saisie_valide = False
    while saisie_valide == False:
        try:
            horizontal = int(input("Entrez le numéro horizontal : ")) - 1
            vertical = int(input("Entrez le numéro vertical : ")) - 1
            if 0 <= horizontal < 3 and 0 <= vertical < 3:
                if grille[horizontal][vertical] == '-':
                    saisie_valide = True
                else:
                    print("\033[1;31mCase déjà occupée\033[0m")
            else:
                print("\033[1;31mCoordonnées hors grille\033[0m")
        except ValueError:
                print("\033[1;31mVeuillez entrer un nombre valide\033[0m")
    return horizontal, vertical

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

def tour_joueur(grille, joueur):
    print(f"\033[1;34mA votre tour de jouer\033[0m")
    affichage(grille)
    horizontal, vertical = saisie_coordonnees(grille)
    grille[horizontal][vertical] = joueur
    return grille

def tour_ordi(grille):
    print(f"\033[1;34mAu tour de l'ordinateur de jouer\033[0m")
    affichage(grille)
    nouvelle_grille, bloque = coup_gagnant(grille, "X")
    if bloque:
        return nouvelle_grille
    nouvelle_grille, gagne = coup_gagnant(grille, "O")
    if gagne:
        return nouvelle_grille
    return positionnement_ordi(grille)


def fonctionnement():
    grille_morpion = creation_grille()
    joueur = "X"
    while victoire(grille_morpion, joueur) != True and est_remplie(grille_morpion) == False:
        if joueur == "X":
            grille_morpion = tour_joueur(grille_morpion, joueur)
        else:
            grille_morpion = tour_ordi(grille_morpion)
        if victoire(grille_morpion, joueur):
            print(f"\033[1;32mVictoire du joueur {joueur}\033[0m")
            affichage(grille_morpion)
            return
        if est_remplie(grille_morpion):
            print("\033[1;33mPartie terminée : match nul\033[0m")
            affichage(grille_morpion)
            return
        joueur = changement_joueur(joueur)

fonctionnement()
        
        


