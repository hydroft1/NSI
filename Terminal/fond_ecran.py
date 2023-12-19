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
        rayon = random.randit(100, 500)
        Cercle((xc, yc), rayon).trace_cairo(ctx, (1, 1, 1))
    image.write_to_png("images.png")