"""Le Donjon de Pyth : point d'entrée."""
from pathlib import Path
import random
from heros import creer_heros, fiche
from donnees import charger_monstres
from combat import creer_monstre, combat

# Dossier du jeu, quel que soit le dossier du terminal
DOSSIER = Path(__file__).parent
DATA = DOSSIER / "data"

def main():
    print("Bienvenue dans le Donjon de Pyth")

    print("Entrez le nom de votre hero :")
    nom = input()
    print("Choisissez la classe de votre hero (1.Guerrier 2.Mage 3.Voleur):")
    choix = input()

    if choix == "1":
        classe = "Guerrier"
    elif choix == "2":
        classe = "Mage"
    elif choix == "3":
        classe = "Voleur"
    else:
        print("Choix invalide")
        return
    print("~~~~~~~~~~~~~~~~~~~")
    heros = creer_heros(nom, classe)
    fiche(heros)
    print("~~~~~~~~~~~~~~~~~~~")
    monstre = creer_monstre(charger_monstres(DATA / "monstres.csv"))
    print(monstre)
    print("~~~~~~~~~~~~~~~~~~~")

    fuite = False
    tour = 0
    while (heros["pv"] > 0 and not fuite and monstre["pv"] > 0):
        tour += 1
        print(f"tour n°{tour}")
        print("1. Attaquer 2.Fuire")
        entrerutilisateur = input()
        if entrerutilisateur == "1":
            combatvaleur = combat(heros, monstre)
            if (combatvaleur == 2):
                print("Defaite")
            elif (combatvaleur == 1):
                print("Victoire")
                return
            else:
                print("~~~~~~~~~~~~~~~~~~~")
        elif entrerutilisateur == "2":
            rng = random.random()
            if (rng < 0.5):
                fuite = True
                print("Vous avez fuit")
        else:
            print("Choix invalide")
            return
    

if __name__ == "__main__":
    main()