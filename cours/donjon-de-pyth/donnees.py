import csv

def convertir(valeur):
    try:
        return int(valeur)
    except ValueError:
        return valeur

def charger_monstres(chemin) -> list[dict]:
    monstres = []
    with open(chemin, "r", encoding="cp1252", newline="") as f:
        for ligne in csv.DictReader(f, delimiter=";"):
            monstre = {cle: convertir(valeur) for cle, valeur in ligne.items()}
            monstres.append(monstre)
    return monstres

def charger_objets(chemin) -> list[dict]:
    objets = []
    with open(chemin, "r", encoding="cp1252", newline="") as f:
        for ligne in csv.DictReader(f, delimiter=";"):
            objets.append(ligne)
    return objets

def index_par_nom(objets) -> dict:
    index = {}
    for objet in objets:
        index[objet["nom"]] = objet
    return index

