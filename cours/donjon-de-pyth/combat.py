import random
from random import randint
from heros import attaque_totale

def creer_monstre(modele) -> dict:
    rng = 15#randint(0, len(modele))
    return {
        "nom" : modele[rng]["nom"],
        "pv" : modele[rng]["pv"],
        "pv_max" : modele[rng]["pv"],
        "attaque" : modele[rng]["attaque"],
        "defense" : modele[rng]["defense"],
        "or" : modele[rng]["or"],
        "xp" : modele[rng]["xp"],
        "niveau_min" : modele[rng]["niveau_min"],
    }

def calculer_degats(attaque, defense) -> int:
    random.seed(-1)
    rng = randint(-2, 2)
    return attaque + rng - defense

def combat(heros, monstre) -> int:
   degatsparheros = calculer_degats(attaque_totale(heros), monstre["defense"])
   monstre["pv"] -= degatsparheros
   print(f"{heros["nom"]} a fait {degatsparheros} degats")
   if (monstre["pv"] > 0):
       degatsparmonstre = calculer_degats(monstre["attaque"], heros["defense"])
       heros["pv"] -= degatsparmonstre
       print(f"{monstre["nom"]} a fait {degatsparmonstre} degats")
       if (heros["pv"] == 0):
           return 2

   if (monstre["pv"] <= 0):
        monstre["pv"] = 0
        heros["or"] += monstre["or"]
        heros["xp"] += monstre["xp"]
        print(f"{heros["nom"]} a gagné {monstre["or"]} d'or et {monstre["xp"]} d'xp")
        return 1


   return 0

       
