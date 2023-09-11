def est_permut(tab):
    """
    Vérifie si une liste donnée contient une permutation des entiers de 1 à n.

    Entrée:
        tab (list): Une liste d'entiers.

    Sortie:
        bool: True si la liste est une permutation, False sinon.
        
    Exemples :
    print(est_permut([1, 2, 3, 4]))  
    print(est_permut([4, 3, 2, 1]))  
    print(est_permut([1, 2, 2, 4]))  
    print(est_permut([1, 2, 3, 5]))  
    print(est_permut([]))            
    """
    n = len(tab)
    
    if n == 0:
        return False  # Retourne False pour la liste vide
    
    appartenance = [False] * n
    
    for i in range(n):
        if tab[i] < 1 or tab[i] > n:
            return False  # Si un élément est en dehors de la plage valide, retourne False
        appartenance[tab[i] - 1] = True
    
    indice = 0
    while indice < n and appartenance[indice]:
        indice += 1
    
    return indice == n

