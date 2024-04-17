def voisins_entrants(adj, x):
    """
    >>> voisins_entrants([[1, 2], [2], [0], [0]], 0)
    [2, 3]
    >>> voisins_entrants([[1, 2], [2], [0], [0]], 1)
    [0]
    """
    voisins_entrants_de_x = []
    
    for sommet, voisins in enumerate(adj):
        if x in voisins:
            voisins_entrants_de_x.append(sommet)
    
    return voisins_entrants_de_x


if __name__ == '__main__':
    import doctest
    doctest.testmod()
