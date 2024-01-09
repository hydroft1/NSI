import collections
import math

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
    # tableau associatif :
    # clé : caractère
    # valeur : fonction
    dico_operations_bin = {"+": lambda a, b: b + a,
                       "-": lambda a, b: b - a,
                       "*": lambda a, b: b * a,
                       "/": lambda a, b: b / a,}
    
    dico_unaires = {"sin": lambda a: math.sin(a),
                    "cos": lambda a: math.cos(a),
                    "tan": lambda a: math.tan(a),
                    "ln": lambda a: math.log(a),
                    "log": lambda a: math.log10(a),
                    "neg" : lambda a: a*(-1),
                    "sq": lambda a: a*a,
                    }

    def __init__(self, s_rpn):
        self.pile_calcul = Pile()
        self.moncalcul =s_rpn
        self.tab_calc = self.moncalcul.split()
        for elt in self.tab_calc:
            if elt in Rpn.dico_operations_bin:
                a = self.pile_calcul.depiler()
                b = self.pile_calcul.depiler()
                res = Rpn.dico_operations_bin[elt](a, b)
                self.pile_calcul.empiler(res)
            elif elt in Rpn.dico_unaires:
                a = self.pile_calcul.depiler()
                res = Rpn.dico_unaires[elt](a)
                self.pile_calcul.empiler(res)
            else:
                self.pile_calcul.empiler(float(elt))
                
    def affichage(self):
        return self.pile_calcul.affichage()
    

if __name__ == "__main__":
    for calcul in ["10 ln",
                   ]:
        clcl = Rpn(calcul)
        print(clcl.affichage())
    