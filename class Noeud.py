class Noeud :
    """
    Classe permettant de représenter les sommets d'un arbre binaire.
    
    :param cle(int):           valeur stockée dans le noeud
    :param sag(Noeud): objet correspondant au sous-arbre gauche du noeud
    :param sad(Noeud):  objet correspondant au sous-arbre droit du noeud
    
    :fct est_feuille():         Fonction déterminant si le noeud ne possède aucun fils.
    """
    def __init__(self, etiquette=None, sag=None, sad=None) :
        self.cle = etiquette
        self.sag = sag
        self.sad = sad
        
    def est_feuille(self) :
        """ Fonction testant si l'objet a ses attributs fils_gauche et fils_droit non-définis """
        return (self.fils_gauche == None) and (self.fils_droit == None)
    
    def __str__(self):
        return f"{(self.sag) + (self.cle) + (self.sad)}"
    
def recherche(abr, element):
    if abr is None : return False
    if abr.Cle == element : return True
    #
    if element < abr.Cle:
        recherche(abr.sag, element)
    else:
        recherche(abr.sad, element)