from collections import deque


class File:
    def __init__(self):
        self._mafile = deque()
    
    def enfiler(self, elt):
        self._mafile.appendleft(elt)
        
    def defiler(self):
        return self._mafile.pop()
    
    def est_vide(self):
        return len(self._mafile) == 0
    
class Noeud():
    def __init__(self, cle, gauche=None, droite=None):
        self.cle = cle
        self.gauche = gauche
        self.droite = droite
        
    
def nombre_chiens(arb, n):
    ...
    
    
nombre_chiens = Noeud()