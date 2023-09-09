def est_permut(tab):
    """
    Vérifie si une liste donnée contient une permutation des entiers de 1 à n.

    Args:
        tab (list): Une liste d'entiers.

    Returns:
        bool: True si la liste est une permutation, False sinon.

    Examples:
        >>> est_permut([1, 2, 3, 4])
        True
        >>> est_permut([4, 3, 2, 1])
        True
        >>> est_permut([1, 2, 2, 4])
        False
        >>> est_permut([1, 2, 3, 5])
        False
        >>> est_permut([])
        False
    """
    n = len(tab)
    appartenance = [False] * n
    
    for i in range(n):
        appartenance[tab[i] - 1] = True
    
    indice = 0
    while indice < n and appartenance[indice]:
        indice += 1
    
    return indice == n
