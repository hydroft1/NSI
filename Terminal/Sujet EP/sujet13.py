# EXERCICE 1
def recherche(elt, tab):
    for indice in range(len(tab)):
        if tab[indice] == elt:
            return indice
    return None

# EXERCICE 2
def insere(tab, a):
    """
    InsÃ¨re l'Ã©lÃ©ment a (int) dans le tableau tab (list)
    triÃ© par ordre croissant Ã  sa place et renvoie le
    nouveau tableau.
    """
    tab_a = [ a ] + tab # nouveau tableau contenant a 
                        # suivi des Ã©lÃ©ments de tab
    i = 0
    while i < len(tab) and a > tab[i]: 
        tab_a[i] = tab_a[i + 1] 
        tab_a[i+1] = a
        i = i + 1 
    return tab_a

print(insere([1, 2, 7, 12, 14, 25], 30))