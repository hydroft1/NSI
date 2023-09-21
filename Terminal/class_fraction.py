class Fraction:
    def __init__(self, n, d):
        self.numerateur = n
        self.denominateur = d
        
    def _somme(self, frc, sgn):
         # sgn = 1 -> addition / -1 -> soustraction
        self.numerateur = self.numerateur * frc.denominateur \
                            + sgn *frc.numerateur * self.denominateur
        self.denominateur = frc.denominateur * self.denominateur
    
    def addition(self, frc):
        self._somme(frc, 1)
        
    def soustraction(self, frc):
        self._somme(frc, -1)
        
    def valeur_decimale(self):
        return self.numerateur / self.denominateur
    
    def __add__(self, frc):
        n= self.numerateur * frc.denominateur \
            + frc.numerateur * self.denominateur
        d = frc.denominateur * self.denominateur
        return Fraction(n, d)
        
    def mystere(self, a, b):
        if a < b:
            a, b = b, a
        
        while b > 0:
            a, b = b, a % b
        
        return a
    
    def __str__(self):
        return str(self.numerateur) + '/' + str(self.denominateur)
    
    def __repr__(self):
        return "Fraction(" + str(self.numerateur) \
            + ", " + str(self.denominateur) + ")"
    
if __name__ == "__main__": 
    f = Fraction(4, 4)
    g = Fraction(-5, 6)
    h = Fraction(8, 7)

    print(f + g + h)


"""
helpers.py -> module de méthode pratique
PG CD -> Plus grand Commun Diviseur ( de deux nombres)

Méthode 1 : sur a = 18 et b = 45
18 = 1x18   45 = 1x45
18 = 2x9    45 = 3x15
18 = 3x6    45 = 5x9
('1', '3', 6, `'9'`, 18)    ('1','3',5,`'9'`,15,45)
' diviseur commun
` PGCD
18/45 = 9x2 / 9x5 = 2/5 

Méthode 2 : si d divise a )
            et d divise b ) -> alors d divise ( a + b et
                                              ( a - b
--------------------------------------------------                                             
| 45 - 18 = 27                                   | 
| d divise 45, (18 et 27) -> deux plus petits    |
|                                                | Méthode 3 : 45 - 2 x 18 = 9 -> reste / division euclidéenne 
| 27 - 18 = 9                                    |
| d divise 45, 27, (18 et 9) -> deux plus petits |
--------------------------------------------------
18 - 9 = 9
d divise 45, 27, 18 et (9) => `plus petits trouvé` 
                                            
"""