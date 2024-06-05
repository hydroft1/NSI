# EX 1 
def moyenne(tab):
    valeur = 0
    for note in range(len(tab)):
        valeur += tab[note]
    return valeur / len(tab)

print(moyenne([1, 2]))

# EX 2
def dichotomie(tab, x):
    """applique une recherche dichotomique pour dÃ©terminer
    si x est dans le tableau triÃ©s tab.
    La fonction renvoie True si tab contient x et False sinon"""

    debut = 0
    fin = len(tab) - 1 
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True 
        if x > tab[m]:
            debut = m + 1 
        else:
            fin = m - 1 
    return False
