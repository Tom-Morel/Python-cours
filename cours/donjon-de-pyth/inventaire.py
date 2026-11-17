from donnees import index_par_nom

def ajouter_objet(heros, objets, nom, quantite) -> None:

    for objet in objets:
        if (objet == nom):
            heros["inventaire"][nom] = heros["inventaire"].get(nom, 0) + quantite

def utiliser_objet(heros, objets, nom) -> str:
    for objetpresent in objets:
        if (objetpresent == nom):
            if (objets[objetpresent]["type"] == "soin"):
                #retirer_objet(heros, nom)
                heros["pv"] = min(heros["pv"] + objets[objetpresent]["bonus"], heros["pv_max"])
                return 1
            elif (objets[objetpresent]["type"] == "arme"):
                if (heros["arme"] == None):
                    heros["arme"] = objetpresent
                    heros["inventaire"][nom] = heros["inventaire"].get(nom, 0) - 1
                else:
                    heros["inventaire"] = heros["arme"]
                    heros["inventaire"][nom] = heros["inventaire"].get(nom, 0) + 1
                    heros["arme"] = objetpresent
                    heros["inventaire"][nom] = heros["inventaire"].get(nom, 0) -1


        
           
"""if heros["inventaire"].get(objetpresent, 0) <= 0:
            return f"Tu n'as pas de {objetpresent}."""
    



 # if (heros["inventare"][i] == heros["inventaire"][""]):

"""def estsoin(objets) -> dict:
    objets_soin = []
    for objet in objets:
        if objet["type"] == "soin":
            objets_soin.append(o)"""