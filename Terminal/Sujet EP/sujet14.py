# EXERCICE 1
def min_et_max(tab):
    imin = tab[0]
    imax = tab[0]
    for i in range(len(tab)):
        if tab[i] > imax:
            imax = tab[i]
        elif tab[i] < imin:
            imin = tab[i]
    return {'min': imin, 'max': imax}

# EXERCICE 2
class Carte:
    def __init__(self, c, v):
        """Initialise les attributs couleur (entre 1 et 4), 
        et valeur (entre 1 et 13). """
        self.couleur = c
        self.valeur = v

    def recuperer_valeur(self):
        """ Renvoie la valeur de la carte : 
        As, 2, ..., 10, Valet, Dame, Roi """
        valeurs = ['As','2', '3', '4', '5', '6', '7', '8', 
                   '9', '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]

    def recuperer_couleur(self):
        """ Renvoie la couleur de la carte 
        (parmi pique, coeur, carreau, trÃ¨fle). """
        couleurs = ['pique', 'coeur', 'carreau', 'trÃ¨fle']
        return couleurs[self.couleur - 1]

class Paquet_de_cartes:
    def __init__(self):
        """ Initialise l'attribut contenu avec une liste des 52
        objets Carte possibles rangÃ©s par valeurs croissantes en
        commenÃ§ant par pique, puis cÅ“ur, carreau et trÃ¨fle. """
        self.contenu = []
        for c in range(1, 5):
            for v in range(1, 14):
                self.contenu.append(Carte(c, v))

    def recuperer_carte(self, pos):
        """ Renvoie la carte qui se trouve Ã  la position pos 
        (entier compris entre 0 et 51). """
        assert pos > -1 and pos < 52, 'paramÃ¨tre pos invalide'
        return self.contenu[pos]
