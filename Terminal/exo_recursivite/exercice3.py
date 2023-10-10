def mediane(tableau):
    n = len(tableau)
    
    if n % 2 == 1:
        # Si le nombre d'éléments est impair, la médiane est au milieu.
        mediane = tableau[n // 2]
    else:
        # Si le nombre d'éléments est pair, la médiane est la moyenne des deux éléments au milieu.
        milieu_gauche = tableau[n // 2 - 1]
        milieu_droite = tableau[n // 2]
        mediane = (milieu_gauche + milieu_droite) / 2
    
    return mediane


T = [1, 2, 3, 4, 5]
T.sort()  
med = mediane(T)
print("La médiane est :", med)
