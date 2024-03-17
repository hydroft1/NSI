class Noeud():
    def __init__(self, cle, gauche=None, droite=None):
        self.cle = cle
        self.gauche = gauche
        self.droite = droite

def trouver_chemins_feuilles(arbre, chemin=[], chemins=[]):
    if arbre is None:
        return

    chemin.append(arbre.cle)

    if arbre.gauche is None and arbre.droite is None:
        chemins.append(list(chemin))

    trouver_chemins_feuilles(arbre.gauche, chemin.copy(), chemins)
    trouver_chemins_feuilles(arbre.droite, chemin.copy(), chemins)

    return chemins

# Exemple d'utilisation
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

chemins = trouver_chemins_feuilles(arbres_chiens)
for chemin in chemins:
    print(" -> ".join(map(str, chemin)))
