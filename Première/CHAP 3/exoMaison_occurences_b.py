# Règle pour avoir 1/1 sur les exos maison : réussir au moins un code demandé. Il y aura à chaque fois un code facile à faire.

""" Code1* :
Comptage du nombre d'occurences supérieures à l'occurence choisie dans une liste non triée
Ne pas utiliser count()
Exemple :
Entrée : L=[3,2,7,1,3,3,4,5,6,3,7,2] et 3
Sortie : Il y a 7 occurences supérieures à l'occurence 5 dans la liste
"""
"""
L = [3,2,7,1,3,3,4,5,6,3,7,2]
occurence_choisie = 5
count = 0
for i in L:
    if i > occurence_choisie:
        count += 1
print("Il y a", count, "occurrences supérieures à l'occurence ", occurence_choisie, "dans la liste ")

"""




""" Code2** :
Comptage du nombre d'occurences (nombres égaux) dans une liste triée
Ne pas utiliser count()
Exemple :
Entrée : L=[1,2,3,4,5,5,5,6,7]
Sortie : 3
On ne se mettra pas dans la situation où il y a plusieurs valeurs identiques, ex : L=[1,2,3,3,3,3,4,5,5,6,7]
"""



L = [1,2,3,4,5,5,5,6,7]
nombre_choisi = 5


premiere_occurrence = -1
derniere_occurrence = -1

# Boucle pour trouver les indices de la première et dernière occurrence
for i in range(len(L)):
    if L[i] == nombre_choisi:
        if premiere_occurrence == -1:
            premiere_occurrence = i
        derniere_occurrence = i

# Vérification si le nombre apparaît dans la liste
if premiere_occurrence != -1 and derniere_occurrence != -1:
    nombre_occurrences = derniere_occurrence - premiere_occurrence + 1
    print("Il y a", nombre_occurrences, "occurrences du nombre", nombre_choisi, "dans la liste.")
else:
    print("Le nombre", nombre_choisi, "n'apparaît pas dans la liste.")
