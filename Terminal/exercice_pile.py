from collections import deque


class Pile:
    def __init__(self):
        self.mapile = list()
        
    def taille(self):
        return len(self.mapile)
        
    def est_vide(self):
        return self.taille() == 0
    
    def empiler(self, element):
        self.mapile.append(element)
    
    def depiler(self):
        return self.mapile.pop()
    
    def sommet(self, element):
        return self.mapile[self.taille() - 1]
        
    def affichage(self):
        s = "["
        for elt in self.mapile:
            s += f" { elt } "
        s += "<"
        return s

class FileDEQ:
    def __init__(self):
        self._mafile = deque()
        
    def taille(self):
        return len(self._mafile)
    
    def est_vide(self):
        return self.taille() == 0
    
    def premier(self):
        return self._mafile[0]
    
    def enfiler(self, e):
        self._mafile.append(e)
    
    def defiler(self):
        return self._mafile.popleft()

def inversion(p):
    f = FileDEQ()
    while not p.est_vide():
        f.enfiler(p.depiler())
    while not f.est_vide():
        p.empiler(f.defiler())   

def inversion_rec(p,f=None):
    if f is None:
        f = FileDEQ()

    if p.vide():
        return
    #
    f.enfiler(p.depiler())
    inversion_rec(p,f)
    p.empiler(f.defiler())
    
    

def test():   
    p = Pile()
    for elt in [3, 8, 5]:
        p.empiler(elt)
    print(p.affichage())
    #p.depiler()
    #print(p.affichage())
    inversion(p)
    print(p.affichage())

test()