def barre_vie(pv, pv_max, largeur=10) -> str:
    pv = max(0, min(pv, pv_max))
    pleines = round(largeur * pv / pv_max)
    vides = largeur - pleines
    return f"[{'█' * pleines}{'░' * vides}] {pv}/{pv_max}"