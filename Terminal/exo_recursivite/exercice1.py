# Exercice 1
def affiche_tab(tab):
    """
    >>> affiche_tab([0,1,2])
    0
    1
    2
    """
    if len(tab) == 0: return
    print(tab[0])
    affiche_tab(tab[1:])
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()