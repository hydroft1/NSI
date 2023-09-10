def est_permut(tab):
    """
    Vérifie si une liste donnée contient une permutation des entiers de 1 à n.

    Entrée:
        tab (list): Une liste d'entiers.

    Sortie:
        bool: True si la liste est une permutation, False sinon.
    """
    n = len(tab)
    appartenance = [False] * n
    
    for i in range(n):
        appartenance[tab[i] - 1] = True
    
    indice = 0
    while indice < n and appartenance[indice]:
        indice += 1
    
    return indice == n
