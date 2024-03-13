"""
    >>> separation_et_concatenation([1, 2, 0, 4, 0, 0, 5, 6, 0])
    [1, 2, 4, 5, 6, 0, 0, 0, 0]
    >>> separation_et_concatenation([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> separation_et_concatenation([0, 0, 0, 0, 0])
    [0, 0, 0, 0, 0]
    >>> separation_et_concatenation([])
    []
    >>> separation_et_concatenation([1, -2, 0, 4, 0, -5, 6, 0, -7])
    [1, -2, 4, -5, 6, -7, 0, 0, 0]
"""

def separation_et_concatenation(liste):
    non_nuls = [x for x in liste if x != 0]
    zero = [x for x in liste if x == 0]
    concatenation = non_nuls + zero
    return concatenation

if __name__ == '__main__':
    import doctest
    doctest.testmod()