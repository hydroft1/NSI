# EXO 1
def jour_suivant(date):
    """
    >>> jour_suivant(("samedi", 21, 10, 1995))
    ('dimanche', 22, 10, 1995)
    >>> jour_suivant(("mardi", 31, 10, 1995))
    ('mercredi', 1, 11, 1995)
    >>> jour_suivant(("mardi", 31, 12, 1995))
    ('mercredi', 1, 1, 1996)
    """
    jours = ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"]
    jours_dans_mois = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

    # Récupération des éléments de la date
    nom_jour, numero_jour, numero_mois, annee = date

    numero_jour_suivant = numero_jour + 1
    if numero_jour_suivant > jours_dans_mois[numero_mois]:
        numero_jour_suivant = 1
        numero_mois += 1
        if numero_mois > 12:
            numero_mois = 1
            annee += 1

    return (jours[(jours.index(nom_jour) + 1) % 7], numero_jour_suivant, numero_mois, annee)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# EXO 2
class Panier():
    def __init__(self):
        pass
    
    def est_vide(self):
        pass
    
    def enfiler(self, e):
        pass
    
    def defiler(self):
        pass
    
    def remplir(self, panier_temp):
        while not panier_temp.estvide():
            article = panier_temp.defiler()
            self.enfiler(article)
            
    def prix_total(self):
        panier_temp = Panier()
        total = 0
        while not self.est_vide():
            article = self.defiler()
            total = total + article[2]
            panier_temp.enfiler(article)
        self.remplir(panier_temp)
        return total
    
    def duree_courses(self):
        if self.est_vide():
            return 0
        
        t0 = t1 = self.defiler()[3]
        while not self.est_vide():
            t1 = self.defiler()[3]
        
        return t1 - t0
        
    
# EXO 3 
