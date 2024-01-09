def p_g_e(liste):
    """
    Cette fonction prend une liste en entrée et retourne le plus grand élément de la liste en utilisant
    l'algorithme de tri à bulles (Bubble Sort).

    Args:
    liste (list): Une liste d'éléments comparables (par exemple, des nombres entiers ou des flottants).

    Returns:
    Comparable: L'élément le plus grand de la liste.

    Exemple d'utilisation:
    >>> p_g_e([4, 2, 9, 1, 5])
    9

    Remarque:
    Cette fonction trie la liste en place en utilisant l'algorithme de tri à bulles, ce qui signifie que
    l'ordre des éléments dans la liste d'origine peut être modifié après l'appel de la fonction.
    """
    n = len(liste)
    for i in range(1, n):
        if liste[i - 1] > liste[i]:
            liste[i - 1], liste[i] = liste[i], liste[i - 1]
    return liste[n - 1]

def mystere(a, b):
    if a < b:
        a, b = b, a
        while b > 0:
            a, b = b, a % b
    return a
