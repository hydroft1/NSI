def car(tab):
    """ Renvoie le premier élément d'un tableau non vide
    """
    return tab[0]
    
def cdr(tab):
    """ Renvoie un tableau des éléments d'un tableau non vide sauf le premier
    
    >>> cdr([1, 2, 3, 4])
    [2, 3, 4]
    """
    # version sans slice
    t = []
    for i in range(1, len(tab)):
        t.append(tab[i])
    return t
    
    # version avec slice
    #return tab[1:]
    
def cons(elt, tab):
    ...



if __name__ == "__main__":
    import doctest
    doctest.testmod()