def fusion(tab1, tab2, comp):
    resultat = []
    i1, i2 = 0, 0
    while i1 < len(tab1) and i2 < len(tab2):
        if comp(tab1[i1], tab2[i2]):
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

def tri_fusion(tab, comp= lambda a,b: a < b):
    n = len(tab)
    #
    if n == 1:
        return tab
    #
    gauche = tab[:n //2]
    droite = tab[n // 2:]
    t_gauche = tri_fusion(gauche)
    t_droite = tri_fusion(droite)
    return fusion(t_gauche, t_droite, comp)

if __name__ == '__main__':
    print(tri_fusion([9,6,2,12,7,8,11,10,4,5,1,3,0]))
    
