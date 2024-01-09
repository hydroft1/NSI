import math as _math

def distance(A, B):
    """ Calculate distance euclidienne between two points A and B en dimiension quelqonque.
    
    Entrées :
        A : tuple
        B : tuple
    
    Précondition :
        A et B de même dimension
        
    Sortie :
        float
    
    >>> math.isclose(distance((0, 0), (1, 1)), math.sqrt(2))
    True
    """

    return _math.sqrt(sum((a - b) ** 2 for a, b in zip(A, B)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    

"""

    n = len(A)
    s = 0
    for i in range(n):
        s += (A[i] - B[i]) **2
    return math.sqrt(s)
    
"""