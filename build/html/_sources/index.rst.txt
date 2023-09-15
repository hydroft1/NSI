.. py:module:: Test

Ce programme génère une image représentant un paysage simple avec un soleil, un arbre et un oiseau.

Classes
=======

.. py:class:: PremierPlan

    Classe pour dessiner des éléments en premier plan.

    .. py:method:: __init__(self, xy, d)

        Initialise un objet PremierPlan avec des coordonnées (xy) et une dimension (d).

    .. py:method:: soleil(self, ctx, rayon, decalage_x, decalage_y)

        Dessine un soleil avec le contexte de dessin (ctx), un rayon, et des décalages en X et en Y.

    .. py:method:: dessiner_arbre(self, ctx)

        Dessine un arbre avec le contexte de dessin (ctx).

    .. py:method:: oiseau(self, ctx, color="black")

        Dessine un oiseau avec le contexte de dessin (ctx) et une couleur spécifiée (par défaut, noir).

.. py:class:: Background

    Classe pour dessiner l'arrière-plan.

    .. py:method:: __init__(self, xy, d)

        Initialise un objet Background avec des coordonnées (xy) et une dimension (d).

    .. py:method:: herbe(self, ctx)

        Dessine de l'herbe dans l'arrière-plan avec le contexte de dessin (ctx).

Exemple d'utilisation
======================

Exemple d'utilisation :

.. code-block:: python

    img = Image.new("RGB", (1200, 1200), color="DarkTurquoise")
    ctx = ImageDraw.Draw(img)

    c = PremierPlan((0, 0), 50)
    b = Background((0, 0), 50)

    b.herbe(ctx)
    c.soleil(ctx, 50, 50, 50)
    c.dessiner_arbre(ctx)
    c.oiseau(ctx)

    img.save("dessin.png")
