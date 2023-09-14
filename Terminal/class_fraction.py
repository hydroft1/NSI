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
        
    
    def __str__(self):
        return str(self.numerateur) + '/' + str(self.denominateur)
    
f = Fraction(4, 4)
g = Fraction(-5, 6)
h = Fraction(8, 7)

print(f + g + h)
