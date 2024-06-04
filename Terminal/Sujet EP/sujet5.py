# EXERCICE 1
def max_et_indice(tab):
    imax = 0
    vmax = tab[0]
    for i in tab:
        if tab[i] > vmax:
            imax = i
            vmax = tab[i]
    return (vmax, imax)

# EXERCICE 2
def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les
    entiers de 1 Ã  n, False sinon
    '''
    n = len(tab)
    # les entiers vus lors du parcours
    vus = [] 

    for x in tab:
        if x < 1 or x > n or x in vus: 
            return False
        vus.append(x) 
    return True

def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui reprÃ©sente 
    un ordre de gÃ¨nes de chromosome
    '''
    # on vÃ©rifie que ordre est un ordre de gÃ¨nes
    assert ... 
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: # le premier n'est pas 1 
        nb = nb + 1
    i = 0
    while i < n-1: 
        if ordre[i]-ordre[i+1] not in [-1, 1]: # l'Ã©cart n'est pas 1 
            nb = nb + 1
        i = i + 1
    if ordre[i] != n: # le dernier n'est pas n 
        nb = nb + 1
    return nb