def mediane(tab, i=0):
    """
    >>> T = [0, 1, 2, 3, 4]
    >>> mediane(T)
    2.0
    >>> T = [0, 1, 2, 3]
    >>> mediane(T)
    1.5
    
    """
    n = len(tab)
    if n <= 2:
        return (tab[0] + tab[n -1]) / 2
    return mediane(tab[1:n - 1])

if __name__ == '__main__':
    import doctest
    doctest.testmod()