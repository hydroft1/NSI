def est_permut(tab):
    n = len(tab)
    appartenance = [False] * n
    
    for i in range(n):
        appartenance[tab[i] - 1] = True
    
    indice = 0
    while indice < n and appartenance[indice]:
        indice += 1
    
    return indice == n



