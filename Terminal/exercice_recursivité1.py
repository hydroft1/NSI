# Exercice 1
def affiche_tab(tab):
    if len(tab) == 0: return
    print(tab[0])
    affiche_tab(tab[1:])
def affiche_tab_v2(tab, i=0):
    if i == len(tab): return
    #
    print(tab[i])
    affiche_tab_v2(tab, i)

# Exercice 2
def reverse(tab):
    if len(tab) == 0: return
    tab.reverse()
    print(tab)
def inversion(tab, inverse):
    if len(tab) == 0: return inverse
    #
    return inversion(tab[1:], [tab[0]] + inverse)
def inversion_v2(tab, i=0):
    n = len(tab)
    if i == n // 2:
        ...
    tab[i], tab[n - 1 - i] = tab[n - 1 - i], tab[i]
    inversion_v2(tab, i + 1)  

# Exercice 3
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

# Exercice 4
def bin_s(tab, e):
    if len(tab) == 1: return tab[0] == e
    #
    indice_milieu = len(tab) // 2
    milieu = tab[indice_milieu]
    if milieu == e: return True
    if milieu < e:
        nv_tab = tab[indice_milieu:]
    else:
        nv_tab = tab[0:indice_milieu]
    return bin_s(nv_tab, e)

# Exercice 5
def est_dans(T, e):
    if len(T) == 0: return False
    #
    return T[0] == e or est_dans(T[1:], e)

def est_dans_v2(T, e):
    if len(T) == 1: return T[0] == e   
    #
    indice_milieu = len(T) // 2
    return est_dans_v2(T[:indice_milieu], e) or\
        est_dans_v2(T[indice_milieu:], e)

# EXERCICE 6
def fib(n):
    if n <= 1: return n
    #
    return fib(n - 1) + fib(n - 2)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
