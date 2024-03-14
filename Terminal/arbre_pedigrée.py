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
    maf = File()
    maf.enfiler((arb, 0))
    
    resultat =  0
    while not maf.est_vide():
        nd, niveau = maf.defiler()
        if niveau == n:
            resultat += 1
        if nd.gauche is not None:
            maf.enfiler(nd.gauche, niveau + 1)
        if nd.droit is not None:
            maf.enfiler(nd.droit, niveau + 1)
    
    return resultat
    
    
arbres_chiens = Noeud("Milka", 
                        Noeud("Eclair", None,
                                Noeud("Etoile",
                                    Noeud("Ulk",
                                        Noeud("Nemo"),
                                        Noeud("Moka")),
                                    Noeud("Maya"))),
                        Noeud("Nougat",
                                Noeud("Neige",
                                    Noeud("Museau")),
                                Noeud("Nuage", 
                                    None, 
                                    Noeud("Noisette")))
)

nombre_chiens(arbres_chiens, 3)