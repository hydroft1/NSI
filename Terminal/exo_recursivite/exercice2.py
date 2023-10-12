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
    

def inversion_v2(tab, i=0):
    """ inversion en place du tableau
    
    >>> T = [0, 1, 2, 3, 4]
    >>> inversion_v2(T)
    >>> T
    [4, 3, 2, 1]
    >>> T = [0, 1, 2, 3]
    >>> inversion_v2(T)
    >>> T
    [3, 2, 1, 0]
    
    """
    n = len(tab)
    if i == n // 2:
        ...
    tab[i], tab[n - 1 - i] = tab[n - 1 - i], tab[i]
    inversion_v2(tab, i + 1)
       

if __name__ == '__main__':
    import doctest
    doctest.testmod()