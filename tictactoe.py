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
            return True
        if grille[0][k] != '-' and grille[0][k] == grille[1][k] == grille[2][k]:
            return True
    if grille[0][0] != '-' and grille[0][0] == grille[1][1] == grille[2][2]:
        return True
    if grille[0][2] != '-' and grille[0][2] == grille[1][1] == grille[2][0]:
        return True
    return False

def changement_joueur(joueur):
    if joueur == 'X':
        return "O"
    else:
        return "X"
        

def fonctionnement():
    grille_morpion = creation_grille()
    joueur = random.choice(joueurs)
    while victoire(grille_morpion) != True and est_remplie(grille_morpion) == False:
        print(f"\033[1;34mAu tour de {joueur} de jouer !\033[0m")
        affichage(grille_morpion)
        horizontal = int(input("Entrez le numéro horizontal : "))-1
        vertical = int(input("Entrez le numéro vertical : "))-1
        while grille_morpion[horizontal][vertical] != '-':
            horizontal = int(input("Entrez le numéro horizontal : "))-1
            vertical = int(input("Entrez le numéro vertical : "))-1
        grille_morpion[horizontal][vertical] = joueur
        if victoire(grille_morpion):
            print(f"\033[1;32mVictoire du joueur {joueur}\033[0m")
            affichage(grille_morpion)
            return
        if est_remplie(grille_morpion):
            print("\033[1;33mPartie terminée : match nul\033[0m")
            affichage(grille_morpion)
            return
        joueur = changement_joueur(joueur)

fonctionnement()
        
        


