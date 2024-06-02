# EXERCICE 1
def maximum_tableau(tab):
    """
    >>> maximum_tableau([98, 12, 104, 23, 131, 9])
    131
    >>> maximum_tableau([-27, 24, -3, 15])
    24
    """
    max_elt = tab[0]
    for i in range(len(tab)):
        if tab[i] > max_elt:
            max_elt = tab[i]
    return max_elt

# EXERICE 2
class Pile:
    """Classe dÃ©finissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie un boolÃ©en indiquant si la pile est vide."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'Ã©lÃ©ment v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'Ã©lÃ©ment placÃ© au sommet de la pile,
        si la pile nâ€™est pas vide. Produit une erreur sinon.
        """
        assert not self.est_vide()
        return self.contenu.pop()

def bon_parenthesage(ch):
    """Renvoie un boolÃ©en indiquant si la chaÃ®ne ch 
    est bien parenthÃ©sÃ©e
    >>> bon_parenthesage("((()())(()))")
    True
    >>> bon_parenthesage("())(()")
    False
    >>> bon_parenthesage("(())(()")
    False
    """
    p = Pile()
    for c in ch:
        if c == '(': 
            p.empiler(c)
        elif c == ')': 
            if p.est_vide():
                return False
            else:
                p.depiler()
    return p.est_vide() 

if __name__ == "__main__":
    import doctest
    doctest.testmod()