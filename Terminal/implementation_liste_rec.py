# Exercice 1 de la fiche
# Implémentation d'un arbre avec un tableau (dynamique)
# La racine est située à l'indice 1 du tableau

# ATTENTION BIEN LIRE ce qui suit :
# Le but est notamment de compléter les codes des fonctions
# de recherche et d'insertion d'un élément.
# Ainsi on considère être dans le cas d'un ABR.
#
# Consigne : Compléter le code ci-dessous : les ...


class ABR:
    def __init__(self):
        """Initialise un ABR vide implémenté avec un tableau.
        Le premier élément du tableau donne sa taille
        """
        self.arbre = [0]

    def __str__(self):
        return str(self.arbre)

    def _recherche(self, element, indice=1):
        """
        Arguments :
        * element : la valeur de l'élément cherché
        * indice : la position à partir de laquelle on cherche (par défaut : 1)

        Renvoie :
        * soit l'indice (positif) de la position de element
        dans l'arbre s'il a été trouvé
        * soit le dernier indice trouvé dans les calculs : cette indice pointe
        alors vers un None du tableau ou pointe en-dehors du tableau

        """
        # on ne doit :
        # - ni dépasser la limite du tableau
        # - ni continuer si on est tombé sur un None (pas de fils possibles)
        # - ni continuer si on a trouvé l'élément

        if indice >= len(self.arbre) \
                or self.arbre[indice] is None \
                or self.arbre[indice] == element:
            return indice

        # appels récursifs vers le fils gauche ou le fils droit
        if element < self.arbre[indice]:
            return self._recherche(element, indice * 2)
        else:
            return self._recherche(element, indice * 2 + 1)

    def rechercher(self, element):
        """Fonction d'interface de recherche d'un élément"""
        indice = self._recherche(element)
        # on renvoie vrai si l'indice est inférieur à la longueur du tableau et
        # si l'élément pointé n'est pas None (et c'est donc l'élément cherché!)
        return indice < len(self.arbre) and self.arbre[indice] == element

    def inserer(self, element):
        """Précondition : l'élément n'est pas dans l'arbre"""

        # L'indice est donc celui d'un None du tableau
        # ou est en-dehors du tableau
        indice = self._recherche(element)

        # si c'est issu d'un None,
        # cette position est celle de l'élément
        if indice < len(self.arbre):
            self.arbre[indice] = element
        # sinon on est en dehors du tableau
        # on doit le compléter avec des None
        # jusqu'à la position trouvée et ajouter l'élément
        else:
            nb_none = indice - len(self.arbre)
            self.arbre += [None] * nb_none
            self.arbre.append(element)
        #
        self.arbre[0] += 1


abr = ABR()
# ne pas oublier que le premier élément est la taille de l'arbre
abr.arbre = [7, 5, 2, 10, 1, 3, None, 15, None, None, None, None, None, None, 12]

# les tests
assert abr.rechercher(10)
assert not abr.rechercher(6)
abr.inserer(12)
assert abr.rechercher(12)
assert abr.arbre == [8, 5, 2, 10, 1, 3, None, 15, None, None, None, None, None, None, 12]
