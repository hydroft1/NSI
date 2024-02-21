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
    
#