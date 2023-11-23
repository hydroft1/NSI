import collections


class Pile:
    def __init__(self):
        self.mapile = collections.deque()
        
    def est_vide(self):
        return len(self.mapile) == 0
    
    def empiler(self, element):
        self.mapile.append(element)
    
    def depiler(self):
        return self.mapile.pop()
    
    def sommet(self, element):
        return self.mapile[len(self.mapile) - 1]
        
    def affichage(self):
        s = "["
        for elt in self.mapile:
            s += f" { elt } "
        s += "<"
        return s
        

class Rpn:
    """
    classe gérant les calculs sous formes de Notation Polonaise Inverse.
    
    On instancie avec une chaîne représentant le calcul à effectuer.
    
    La classe utilise une pile.
    """
    def __init__(self, s_rpn):
        self.moncalcul =s_rpn
        