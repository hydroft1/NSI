# EXERCICE 1
def couples_consecutifs(tab):
    resultat = []
    for i  in range(len(tab) -1):
        if tab[i] + 1 == tab[i + 1]:
            resultat.append((tab[i], tab[i + 1]))
    return resultat

assert couples_consecutifs([1, 4, 3, 5]) == []
assert couples_consecutifs([1, 4, 5, 3 ]) == [(4, 5)]
couples_consecutifs([5, 1, 2, 3, 8, -5, -4, 7]) == [(1, 2), (2, 3), (-5, -4)]

# EXERCICE 2

def colore_comp1(M, i, j, val):
    if M[i][j] != 1:
        return

    M[i][j] = val

    if i-1 >= 0: 
        colore_comp1(M, i-1, j, val)
    if i+1 < len(M):
        colore_comp1(M, i+1, j, val) 
    if j-1 >= 0 :
        colore_comp1(M, i, j-1, val) 
    if j+1 < len(M[0]):
        colore_comp1(M, i, j+1, val)