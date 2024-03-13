def sacados(tab_p, tab_v, pmax):
    """ Renvoie la valeur maximale du sac à dos

    params :
     - tab_p : tableau des poids
     - tab_v : tableau des valeurs
     - pmax : poids total admissible
     
    >>> sacados([3, 8, 2, 4, 1], [50, 65, 10, 70, 10], 10)
    140
    """

    # nombre d'objets
    n = len(tab_p)
    tab_optimise = [[0 for _ in range(pmax + 1)] for _ in range(n)]
    # 1ère ligne
    for i_poids in range(tab_p[0], pmax + 1):
        tab_optimise[0][i_poids] = tab_v[0]
    # autres lignes
    for i_objet in range(1, n):
        # on ne prend pas l'objet
        for i_poids in range(1, tab_p[i_objet]):
            tab_optimise[i_objet][i_poids] = tab_optimise[i_objet - 1][i_poids]
        for i_poids in range(tab_p[i_objet], pmax + 1):
            # on prend ou pas l'objet
            tab_optimise[i_objet][i_poids] = max(
                tab_optimise[i_objet - 1][i_poids],
                tab_v[i_objet] + tab_optimise[i_objet - 1][i_poids - tab_p[i_objet]])
    
    x = [0] * n
    colonne = pmax
    for ligne in range(n - 1, 0, -1):
        if tab_optimise[ligne][colonne] != tab_optimise[ligne - 1][colonne]:
            # on a pris l'objet
            x[ligne] = 1
            colonne = colonne - tab_p[ligne]
    if tab_optimise[0][colonne] != 0:
        x[0] = 1    
        
            
    # on renvoie la valeur en bas à droite
    return tab_optimise[n - 1][pmax]



if __name__ == "__main__":
    import doctest
    doctest.testmod()