"""Le Donjon de Pyth : point d'entrée."""
from pathlib import Path
from heros import *
from donnees import *

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

    #heros = creer_heros(nom, classe)
    #fiche(heros)

    monstres = charger_monstres(DATA / "monstres.csv")
    print(monstres[0]["nom"])

    objets = charger_objets(DATA / "objets.csv")
    print(objets[0])
    print(index_par_nom(objets)["Potion"])
if __name__ == "__main__":
    main()