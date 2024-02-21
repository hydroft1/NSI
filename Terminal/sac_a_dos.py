# programmation du problème du sac-à-dos
# de manière "dynamique", c'est à dire en optimisant
# avec un tableau

def sacados(tab_p, tab_v, pmax):
    """ Résout le problème du sac à dos en renvoyant la valeur maximale des objets à prendre
    
    Arguments : 
    tab_p : tableau d'entiers des masses des objets
    tab_v : tableau des valeurs des objets
    pmax : masse maximale par le sac à dos
    
    Précondition :
    tab_p et tab_v sont de même taille
    
    Renvoi :
    La valeur max du sac à dos
    
    
    
    """
    
    # nombre d'objets
    n = len(tab_p)
    # initialisation
    tab_optimise = [[0 for j in range(pmax + 1)]
                    for i in range(n)] 
    
    #1ere ligne
    for poids in range(tab_p[0], pmax + 1):
        tab_optimise[0][poids] = tab_v[0]
    #1ere colonne
    # les zéros y sont déjà 
    # parcours de la matrice élément par élément
    # ligne par ligne
    for i_objet in range(1, n):
        # l'objet est trop lourd pour le sac à dos
        # on le prend pas
        for i_poids in range(1, tab_p[i_objet]):
            tab_optimise[i_objet][i_poids] = tab_optimise[i_objet - 1][i_poids]
        for i_poids in range(tab_p[i_objet], pmax + 1):
            oui_objet = tab_v[i_objet] \
            + tab_optimise[i_objet - 1][i_objet- tab_p[i_objet]]
            non_objet = tab_optimise[i_objet - 1][i_poids]
            tab_optimise[i_objet][i_poids] = max(oui_objet, non_objet)
    return tab_optimise[n - 1][pmax]

tab_p = [5, 3, 1, 4]
tab_v = [100, 55, 18, 70]
pmax = 7

print(sacados(tab_p, tab_v, pmax))