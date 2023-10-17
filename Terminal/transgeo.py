import math as _math


def milieu(A, B):
    """
    :param tuple(float) A: tuple de coords de A
    :param tuple(float) B: tuple de coords de B
    """
    return tuple((a + b) / 2 for a, b in zip(A, B))


def bary(A, B, k):
    """
    permet de disposer d'un point sur la droite (AB)
    :param tuple(float) A: tuple de coords de A
    :param tuple(float) B: tuple de coords de B
    :param float k: coefficient
    """
    return tuple(a * k + b * (1 - k) for a, b in zip(A, B))


def translation(A, angle_degre, longueur):
    """renvoie les coordonnées du point B, image de A dans une
    translation de vecteur défini par l'angle fait par rapport à
    l'axe des abscisses et de longueur précisée.

    :param A tuple(float): coords du point de départ
    :param angle_degre integer: angle du segment /axe des abscisses
    :param longueur float: longueur AB
    :rtype: tuple(float)
    """
    angle_radian = _math.radians(angle_degre)
    return (A[0] + longueur * _math.cos(angle_radian),
            A[1] + longueur * _math.sin(angle_radian))


def rotation60(M, centre):
    """renvoie les coordonnées du point image de M dans la rotation de
    centre précisé et d'angle de mesure 60° dans le sens direct.

    :param M tuple(float): coords du point à transformer
    :param centre tuple(float): coords du centre de rotation
    :rtype: tuple(float)
    """
    rc32 = _math.sqrt(3) / 2
    return (centre[0] + (M[0] - centre[0]) / 2 - rc32 * (M[1] - centre[1]),
            centre[1] + (M[1] - centre[1]) / 2 + rc32 * (M[0] - centre[0]))


def rotation90(M, O, sens=1):
    """renvoie les coordonnées de l'image de M dans une rotation d'un
    quart de tour de centre O dans un sens ou dans l'autre

    :param tuple(float) M: coords du point à transformer
    :param tuple(float) O: coords du centre de la rotation
    :rtype: tuple(float)

    >>> rotation90((1, 0), (0, 0))
    (0, 1)
    >>> rotation90((4, 5), (3, 4))
    (2, 5)
    >>> rotation90((4, 5), (3, 4), -1)
    (4, 3)
    """
    return (O[0] + sens * (O[1] - M[1]), O[1] + sens * (- O[0] + M[0]))


def rotation(M, angle_degre, centre):
    """renvoie les coordonnées de l'image de M dans une rotation d'angle_degre
    (en degrés) de centre centre

    :param tuple(float) M: coords du point à transformer
    :param tuple(float) angle_degre: angle exprimé en degrés
    :param tuple(float) centre: coords du centre de la rotation
    :rtype: tuple(float)
    """
    angle_radian = _math.radians(angle_degre)
    c, s = _math.cos(angle_radian), _math.sin(angle_radian)
    X = centre[0] + (M[0] - centre[0]) * c - (M[1] - centre[1]) * s
    Y = centre[1] + (M[1] - centre[1]) * c + (M[0] - centre[0]) * s
    return (X, Y)


def homothetie(M, centre, rapport):
    """renvoie les coordonnées de l'image de M dans l'homothétie 
    de centre O et de rapport k

    :param tuple(float) M: coords du point à transformer
    :param tuple(float) O: coords du centre de la rotation
    :param float k: rapport de l'homothétie
    :rtype: tuple(float)

    >>> homothetie((1, 0), (0, 0), 3)
    (3, 0)
    >>> homothetie((3, 2), (1, 1), 3)
    (7, 4)
    """
    X = centre[0] + rapport * (M[0] - centre[0])
    Y = centre[1] + rapport * (M[1] - centre[1])
    return (X, Y)

# Versions complexes


def milieuc(zA, zB):
    """version complexe (avec des affixes)
    :param complex zA: point A
    :param complex zB: point B
    """
    return (zA + zB) / 2


def baryc(zA, zB, k):
    """version complexe (avec des affixes)
    :param tuple(float) zA: point A
    :param tuple(float) zB: point B
    :param float k: coefficient
    """
    return k * zA + (1 - k) * zB


def translationc(zM, zvecteur):
    """version complexe (avec des affixes)
    :param complex zM: point à transformer
    :param complex zvecteur: vecteur de translation
    """
    return zM + zvecteur


def homothetiec(zM, zcentre, rapport):
    """version complexe (avec des affixes)
    :param complex zM: point à transformer
    :param complex zcentre: centre de l'homothétie
    :param float rapport: rapport de l'homothétie
    """
    return zcentre + rapport * (zM - zcentre)


def rotationc(zM, angle_degre, zcentre):
    """version complexe (avec des affixes)
    :param complex zM: point à transformer
    :param float angle_degre: angle de rotation exprimé en degrés
    :param complex zcentre: centre de l'homothétie
    """
    angle_radian = _math.radians(angle_degre)
    e_i_theta = _math.cos(angle_radian) + _math.sin(angle_radian) * 1j
    return zcentre + e_i_theta * (zM - zcentre)