# EXERCICE 1
def nombre_de_mots(phrase):
    n = len(phrase)
    valeur = 0
    for i in phrase:
        if i == ' ':
            valeur += 1
    if phrase[-1] == '.':
        return valeur + 1
    else:
        return valeur

# EXERCICE 2
class Noeud:
    def __init__(self, etiquette):
        '''MÃ©thode constructeur pour la classe Noeud.
        CrÃ©e une feuille d'Ã©tiquette donnÃ©e.'''
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None

    def inserer(self, cle):
        '''InsÃ¨re la clÃ© dans l'arbre binaire de recherche
        en prÃ©servant sa structure.'''
        if cle < self.etiquette:
            if self.gauche != None:
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle) 
        else:
            if self.droit != None:
                self.droit.inserer(cle)
            else:
                self.droit = Noeud(cle) 