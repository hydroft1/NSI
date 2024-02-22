# Recherche pour la dernière occurrence
def recherche_derniere_occ(tab, n):
    """
    >>> recherche_derniere_occ([1, 2, 3, 4, 5], 4)
    3
    >>> recherche_derniere_occ([1, 2, 3, 4, 4, 5, 6, 4, 7], 4)
    7
    """
    indice = len(tab)
    for i in range(0, len(tab)):
        if tab[i] == n:
            indice = i
    return indice

  
# recherche pour la première occurrence
def recherche_premiere_occ(tab, n):
    """
    >>> recherche_premiere_occ([1,2,3,4,4,5,6,4,7], 4)
    3
    >>> recherche_premiere_occ([1,2,3,4,5,6,7], 6)
    5
    >>> recherche_premiere_occ([9, 5, 4, 7, 2, 3], 7)
    3
    """
    indice = len(tab)
    i = 0
    while i < len(tab):
        if tab[i] == n:
            indice = i
            break
        i += 1
    return indice


if __name__ == "__main__":
    import doctest
    doctest.testmod()