infini = float("inf")
def rendu_rec(pieces, somme_a_rendre):
    """
    >>> rendu_rec((50, 20, 10, 5, 2, 1), 17)
    3
    >>> rendu_rec((30, 24, 12, 6, 3, 1), 48)
    2
    """
    if somme_a_rendre < 0:
        return infini
    if somme_a_rendre == 0:
        return 0
    #
    nb_pieces = infini
    for p in pieces:
        nb_pieces = min(nb_pieces, 1 + rendu_rec(somme_a_rendre - p))
    
    return nb_pieces

def rendu_dyn(pieces, somme_a_rendre):
    """
    >>> rendu_dyn((50, 20, 10, 5, 2, 1), 17)
    3
    >>> # rendu_dyn((30, 24, 12, 6, 3, 1), 48)
    >>> rendu_dyn((5, 2, 1), 9)
    [0, 1, 1, 2, 2, 1, 2, 2, 3, 3]
    """
    tab_rendu = [infini for _ in range(somme_a_rendre + 1)]
    tab_rendu[0] = 0
    for i in range(1, somme_a_rendre + 1):
        for p in range(len(pieces)):
            pc = pieces[p]
            if pc <= i:
                tab_rendu[i] = min(tab_rendu[i],
                                   1 + tab_rendu[i - pc])
    return tab_rendu[somme_a_rendre]

if __name__ == '__main__':
    import doctest
    doctest.testmod
    