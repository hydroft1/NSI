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

def affiche_tab_v2(tab, i=0):
    """
    >>> affiche_tab_v2([0,1,2])
    0
    1
    2
    """
    if i == len(tab): return
    #
    print(tab[i])
    affiche_tab_v2(tab, i)

  

if __name__ == "__main__":
    import doctest
    doctest.testmod()