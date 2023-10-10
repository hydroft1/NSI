def reverse(tab):
    """
    >>> reverse([0,1,2])
    [2, 1, 0]
    """
    if len(tab) == 0: return
    tab.reverse()
    print(tab)
    
    
def inversion(tab, inverse):
    """
    >>> T = inversion([0, 1, 2])
    >>> T
    [2, 1, 0]
    
    """
    if len(tab) == 0: return inverse
    #
    return inversion(tab[1:], [tab[0]] + inverse)
    


if __name__ == '__main__':
    import doctest
    doctest.testmod()