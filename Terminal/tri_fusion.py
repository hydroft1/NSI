def fusion(tab1, tab2):
    resultat = []
    i1, i2 = 0, 0
    while i1 < len(tab1) and i2 < len(tab2):
        if tab1[i1] < tab2[i2]:
            resultat.append(tab1[i1])
            i1 += 1
        else:
            resultat.append(tab2[i2])
            i2 += 1
    
    if i1 == len(tab1):
        resultat += tab2[i2:]
    else:
        resultat += tab1[i1:]
    
    return resultat

def tri_fusion(tab):
    n = len(tab)
    #
    if n == 1:
        return tab
    #
    gauche = tab[:n //2]
    droite = tab[n // 2:]