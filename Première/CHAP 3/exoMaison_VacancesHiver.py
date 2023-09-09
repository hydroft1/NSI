# Règle pour avoir 1/1 sur les exos maison : réussir au moins un code demandé. Il y aura à chaque fois un code facile à faire.

""" Code1* :
Créez un dictionnaire qui donne le nombre d'occurence de chaque nombre présent dans la liste.
Vous pouvez utiliser count() et max()
Exemple :
Entrée : L=[7,3,2,6,7,3,0,3,3,5,2,6,7,2,0]
Sortie : D={0:2,1:0,2:3,3:4,4:0,5:1,6:2,7:3}
"""

"""
def count_occurrences(L):
    D = {}
    for item in L:
        if item in D:
            D[item] += 1
        else:
            D[item] = 1
    return D

L = [7,3,2,6,7,3,0,3,3,5,2,6,7,2,0]
D = count_occurrences(L)
print(D) # L'odre d'afichage n'est pas croissant 
"""





""" Code2** :
Comptage du nombre d occurences maximum dans le dictionnaire du code1
Ne pas utiliser count()
Exemple :
Entrée : D={0:2,1:0,2:3,3:4,4:0,5:1,6:2,7:3}
Sortie : il y en a 4 occurences du nombre 3 dans la liste
"""


"""
max_occurrence = max(D.values())

print("Il y a", max_occurrence, "occurences du nombre", [key for key, value in D.items() if value == max_occurrence][0], "dans la liste.")
"""






""" Code3** : = code1 sans utiliser count() et max()
Créez un dictionnaire qui donne le nombre d'occurence de chaque nombre présent dans la liste.
Vous ne pouvez pas utiliser count() et max()
Exemple :
Entrée : L=[7,3,2,6,7,3,0,3,3,5,2,6,7,2,0]
Sortie : D={0:2,1:0,2:3,3:4,4:0,5:1,6:2,7:3}
"""
"""
def count_occurrences(L):
    D = {}
    for item in L:
        if item in D:
            D[item] += 1
        else:
            D[item] = 1
    return D

L = [7,3,2,6,7,3,0,3,3,5,2,6,7,2,0]
D = count_occurrences(L)
print(D) # L'odre d'afichage n'est pas croissant 
"""




""" Code4*** :
Comptage du nombre d occurences maximum dans une liste non triée
Ne pas utiliser count()
Exemple :
Entrée : L=[7,3,2,6,7,3,0,3,3,5,2,6,7,2,0]
Sortie : il y en a 4 occurences du nombre 3 dans la liste
"""
def count_occurrences(L):
    D = {}
    for item in L:
        if item in D:
            D[item] += 1
        else:
            D[item] = 1
    max_value = 0
    max_key = 0
    for key, value in D.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key, max_value

L = [7,3,2,6,7,3,0,3,3,5,2,6,7,2,0]

max_key, max_value = count_occurrences(L)

print("Il y a", max_value, "occurences du nombre", max_key, "dans la liste.")
