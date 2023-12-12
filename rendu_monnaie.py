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


if __name__ == '__main':
    import doctest
    doctest.testmod
    