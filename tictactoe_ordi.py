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
        if grille[k][0] == joueur and grille[k][0] == grille[k][1] == grille[k][2]:
            return True
        if grille[0][k] == joueur and grille[0][k] == grille[1][k] == grille[2][k]:
            return True
    if grille[0][0] == joueur and grille[0][0] == grille[1][1] == grille[2][2]:
        return True
    if grille[0][2] == joueur and grille[0][2] == grille[1][1] == grille[2][0]:
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

def test_victoire_ordi(grille):
    for i in range(3):
        for j in range(3):
            if grille[i][j] == "-":
                grille[i][j] = "O"
                if victoire(grille, "O") == False:
                    grille[i][j] = "-"
                else:
                    return grille, True
    return grille, False

def test_victoire_joueur(grille):
    for i in range(3):
        for j in range(3):
            if grille[i][j] == "-":
                grille[i][j] = "X"
                if victoire(grille, "X") == False:
                    grille[i][j] = "-"
                else:
                    grille[i][j] = "O"
                    return grille, True
    return grille, False

def positionnement_ordi(grille):
    est_place = False
    while est_place == False:
        h = random.randint(0, 2)
        v = random.randint(0, 2)
        if grille[h][v] == "-":
            grille[h][v] = "O"
            est_place = True
            return grille
    return

def tour_joueur(grille, joueur):
    print(f"\033[1;34mA votre tour de jouer\033[0m")
    affichage(grille)
    horizontal, vertical = saisie_coordonnees(grille)
    grille[horizontal][vertical] = joueur
    return grille

def tour_ordi(grille):
    print(f"\033[1;34mAu tour de l'ordinateur de jouer\033[0m")
    affichage(grille)
    nouvelle_grille, est_place = test_victoire_joueur(grille)
    if est_place == False:
        nouvelle_grille, est_place = test_victoire_ordi(grille)
        if est_place == True:
            return nouvelle_grille
        else:
            nouvelle_grille = positionnement_ordi(grille)
            return nouvelle_grille
    else:
        return nouvelle_grille


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
        
        


