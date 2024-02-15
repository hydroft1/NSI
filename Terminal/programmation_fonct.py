# exercice 1
""""""
def car(tab):
    """Renvoie le premier élément d'un tableau non vide

    """
    return tab[0]


def cdr(tab):
    """Renvoie un tableau des éléments d'un tableau non vide sauf
    le premier

    >>> cdr([1])
    []
    >>> cdr([1, 2, 3, 4])
    [2, 3, 4]
    """
    # version sans slice
    t = []
    for i in range(1, len(tab)):
        t.append(tab[i])
    return t
    # version avec slice
    # return tab[1:]

def mon_map(f, tab):
    return [f(tab[i]) for i in range(len(tab))]


def mon_map_rec(f, tab):
    """
    >>> mon_map_rec(lambda x: x**2, cons(1, cons(2, cons(3, cons(4, cons(5, []))))))
    [1, 4, 9, 16, 25]
    """
    if tab == []:
        return tab
    #
    return cons(f(car(tab)), mon_map_rec(f, cdr(tab)))


def mon_filter(f, tab):
    """
    >>> mon_filter(lambda x : x>=0, [-3, -2, 0, 3, -5])
    [0, 3]
    """
    return [elt for elt in tab if f(elt)]

def cons1(elt, tab):
    """concatène l'élément elt au tableau tab en le plaçant en 1re
    position

    """
    tmp1 = tab[0]
    for i in range(len(tab) - 1):
        tmp = tab[i + 1]
        tab[i + 1] = tmp1
        tmp1 = tmp
    tab.append(tmp1)
    tab[0] = elt


def cons2(elt, tab):
    """concatène l'élément elt au tableau tab en le plaçant en 1re
    position

    """
    dernier = tab[len(tab) - 1]
    for i in range(len(tab) - 1):
        tab[len(tab) - i - 1] = tab[len(tab) - i - 2]
    tab.append(dernier)
    tab[0] = elt


def cons(elt, tab):
    return [elt] + tab


# Exercice 2

def longeur(tab):
    if tab == []: return 0
    #
    return 1 + longeur(cdr(tab))

def somme(tab):
    """
    >>> somme([1, 2, 3, 4])
    10
    """
    res = 0
    def _somme_res(res):
        if tab == []: return res
        res += car(tab)
        tab = cdr(tab)
        _somme_res()
    #
    _somme_res()
    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod()
