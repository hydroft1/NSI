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
        s = ">"
        stock = Pile()
        while not self.est_vide():
            elt = self.depiler()
            stock.empiler(elt)
            s += f" { elt } "
        while not stock.est_vide():
            elt = stock.depiler()
            self.empiler(elt)
        return s + "]"        

class Rpn:
    """
    classe gérant les calculs sous formes de Notation Polonaise Inverse.
    
    On instancie avec une chaîne représentant le calcul à effectuer.
    
    La classe utilise une pile.
    """
    tab_op = ["+", "-", "*", "/"] 
    
    def __init__(self, s_rpn):
        self.pile_calcul = Pile()
        self.moncalcul =s_rpn
        self.tab_calc = self.moncalcul.split()
        for elt in self.tab_calc:
            if elt in self.tab_op:
                ...
            else:
                ...
    
    def _additation(self):
        pass
        
    def _soustractions(self):
        pass
    
    def _multiplication(self):
        pass
    
    def _division(self):
        pass