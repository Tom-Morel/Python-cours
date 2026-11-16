heros = {
    "nom" : "Ada",
    "classe" : "Guerrier",
    "pv" : 40,
    "pv_max" : 40,
    "attaque" : 6,
    "defense" : 3,
    "or" : 20,
    "xp" : 0,
    "niveau" : 1,
    "inventaire" : {"Potion" : 2},
    "arme" : None,
    "armure" : None,
    "salle" : 1,
    }

CLASSES = {
    "Guerrier" : {"pv" : 40, "attaque" : 6, "defense" : 3, "or" : 20},
    "Mage" : {"pv" : 28, "attaque" : 8, "defense" : 1, "or" : 30},
    "Voleur" : {"pv" : 32, "attaque" : 6, "defense" : 2, "or" : 50},
    }

def creer_heros(nom, classe) -> dict:
    stats = CLASSES[classe]
    return {
        "nom" : nom,
        "classe" : classe,
        "pv" : stats[pv]
        "pv_max" : stats[pv_max],
        "attaque" : stats[attaque],
        "defense" : stats[defense],
        "or" : stats[or],
        "xp" : 0,
        "niveau" : 1,
        "inventaire" : {"Potion" : 2},
        "arme" : None,
        "armure" : None,
        "salle" : 1,
    }

def attaque_totale(heros) -> int:
    bonus = heros["arme"]["attaque"] if heros["arme"] else 0 
    return heros["attaque"] + bonus;

def defense_totale(heros) -> int:
    bonus = heros["armure"]["defense"] if heros["armure"] else 0 
    return heros["defense"] + bonus;

def fiche(heros) -> str:
    print f"{heros["nom"]} le {heros["classe"]} - niveau {heros["niveau"]} ({heros["xp"]} XP \n)"
    print f"\t PV : {heros[pv]}/{heros[pv_max]} \n"
    print f"\t Attaque : {attaque_totale(heros)} (arme : {heros[arme]}) \n"
    print f"\t Défense : {defense_totale(heros)} (armure : {heros{armure}}) \n"
    print f"\t Or : {heros["or"]} \n"
    print f"\t Sac : {heros["invertaire"]} \n"