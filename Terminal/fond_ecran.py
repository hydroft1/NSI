"""Ce module définit la classe Cercle utilisable avec pycairo,
l'interface Cairo de python.

"""


import math


class Cercle:
    """Classe permettant de définir et dessiner des cercles

    """

    def distance(xy0, xy1):
        """Méthode statique de calcul de distances entre deux
        points du plan.

        Arguments :
            xy0 : tuple d'entiers des coordonnées du premier point
            xy1 : tuple d'entiers des coordonnées du deuxième point

        """
        return math.sqrt((xy1[0] - xy0[0]) ** 2 + (xy1[1] - xy0[1]) **2)

    def __init__(self, centre, rayon):
        """Constructeur

        Arguments :
            position : tuple de float des coordonnées du centre du cercle
            rayon : entier définissant le rayon du cercle en pixels

        """
        self.centre = centre
        self.rayon = rayon

    def appartient_disque(self, point):
        """Vérifie qu'un point appartient au disque défini par le
        cercle

        Argument :
            point : tuple d'entiers des coordonnées du point à tester

        Renvoi : booléen

        """
        return self.distance(self.centre, point) <= self.rayon

    def trace_cairo(self, ctx, couleur):
        """Trace un cercle dans un contexte Cairo avec la couleur donné

        Arguments :
            ctx : objet Context Cairo sur lequel le dessin sera à tracer
            couleur : tuple de float RGB correspondant à la couleur de tracé
                      chaque canal prend une valeur comprise entre 0 et 1

        """
        ctx.set_source_rgb(*couleur)
        ctx.arc(*self.centre, self.rayon, 0, 2 * math.tau)
        ctx.stroke()
        
if __name__ == '__main__':
    import cairo
    import random
    WIDTH = 1920
    HEIGHT = 1080
    image = cairo.ImageSurface(cairo.FORMAT_RGB24, WIDTH, HEIGHT)
    ctx = cairo.Context(image)
    ctx.set_source_rgb(0, 0, 0)
    ctx.paint()
    ctx.set_line_width(4)
    
    for _ in range(50):
        xc = random.randrange(0, WIDTH)
        yc = random.randrange(0, HEIGHT)
        rayon = random.randint(100, 500)
        Cercle((xc, yc), rayon).trace_cairo(ctx, (1, 1, 1))
    image.write_to_png("images.png")
    
"""Ce module définit la classe Fond de création d'une image
destinée à servir de fond d'écran.

Elle utilise la classe Cercle et permet de construire une image
faite de cercles qui ne se chevauchent pas.

La surface de dessin est gérée avec pycairo.

"""


import random
import cairo


class Fond:
    """Cette classe permet de créer une image considérée comme un
    fond d'écran.

    Chaque fond peut être sauvegardée en format PNG.

    """

    def __init__(self, largeur=1920, hauteur=1080, couleur=(0, 0, 0)):
        """Constructeur

        Arguments :
            largeur (optionnel) : largeur de l'image (par défaut celle de FHD)
            hauteur (optionnel) : hauteur de l'image (par défaut celle de FHD)
            couleur (optionnel) : tuple de float RGB correspondant à la couleur
                                  de tracé, chaque canal prend une valeur
                                  comprise entre 0 et 1.
                                  Par défaut (0, 0, 0) : noir

        """
        self.largeur = largeur
        self.hauteur = hauteur
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32,
                                           self.largeur, self.hauteur)
        self.ctx = cairo.Context(self.surface)
        self.ctx.set_source_rgb(*couleur)
        self.ctx.paint()
        self.cercles = []

    def est_dans_un_cercle(self, point):
        """Vérifie qu'un point donné par ses coordonnées appartient
        à l'un des cercles déjà construit.

        Arguments :
            point : tuple d'entiers des coordonnées du point à tester

        Renvoi : booléen

        """
        dedans = False
        i = 0

        while i < len(self.cercles) and not dedans :
            un_cercle = self.cercles[i]
            dedans = Cercle.appartient_disque(point)
            i += 1

        return dedans

    def rayon_max_bords(self, position):
        """Renvoie la distance la plus courte des quatre bords~: on
        s'assure que le cercle soit intégralement visible.

        Arguments :
            position : tuple d'entiers des coordonnées du centre du cercle

        Renvoi : entier

        """
        dist_gauche = position[0]
        dist_droite = self.largeur - 1 - position[0]
        dist_bas = self.hauteur - 1 - position[1]
        dist_haut = position[1]

        return min(dist_gauche, dist_droite, dist_bas, dist_haut)

    def rayon_max_cercles(self, position):
        """Détermine le rayon maximal du cercle possible à la
        position donnée en évitant les chevauchements avec ce qui
        existe déjà et en s'assurant que le cercle soit
        intégralement visible.

        Arguments :
            position : tuple d'entiers des coordonnées du centre du cercle

        Renvoi : entier

        """
        # on ne s'interdit rien au départ !
        r_max = float('inf')
        for c in self.cercles:
            nv_rayon_possible = Cercle.distance(position, c.centre) - c.rayon
            r_max = min(r_max, nv_rayon_possible)
        return r_max

    def tracer_cercles(self, effectif, couleur):
        """Construit les cercles en nombre demandé. Les cercles ne
        se chevauchent pas et sont intégralement tracés dans
        l'image.

        Si trop de cercles sont demandés, l'algorithme choisi ne
        permet pas d'assurer une fin rapide, voire une fin tout
        court...

        Arguments :
            nb : nombre de cercles à tracer
            couleur : tuple de float RGB correspondant à la couleur de tracé
                      chaque canal prend une valeur comprise entre 0 et 1

        Renvoi : None

        """
        for _ in range(effectif):

            position_valide = False
            while not position_valide:
                x, y = random.randrange(0, self.largeur), random.randrange(0, self.hauteur)
                position_valide = not self.est_dans_un_cercle((x, y))

            position = (x, y)
            # on détermine le rayon :
            rayon = rayon = min(...,
                        self.rayon_max_cercles(...),
                        self.rayon_max_bords(...))
            nouveau_cercle = Cercle.Cercle(..., ...)
            # on trace maintenant le cercle :
            ...
            # on l'ajoute aux cercles déjà tracés
            self.cercles.append(nouveau_cercle)

    def sauvegarder(self, nom_fichier_png):
        """Permet l'enregistrement de l'image dans un fichier PNG.

        Argument :
            nom_fichier_png : chaîne de caractères du nom de fichier,
                              préciser l'extension ".png" dans le nom

        """
        self.surface.write_to_png(nom_fichier_png)