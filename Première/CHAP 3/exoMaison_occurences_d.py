# Règle pour avoir 1/1 sur les exos maison : réussir au moins un code demandé. Il y aura à chaque fois un code facile à faire.

""" Code1* :
Créez une liste à partir du dictionnaire du nombre d'occurence de chaque chiffre présent dans la liste.
Vous pouvez utiliser count() et max()
Exemple :
Entrée : D={0:0,1:1,2:2,3:4,4:1,5:1,6:1,7:2}
Sortie : L=[1,2,2,3,3,3,3,4,5,6,7,7]
"""
"""
def create_list(dictionnaire):
  resultat = []
  for key, value in dictionnaire.items():
    for dictionnaire in range(value):
      resultat.append(key)
  return resultat

dictionnaire = {0:0, 1:1, 2:2, 3:4, 4:1, 5:1, 6:1, 7:2}
print(create_list(dictionnaire))
"""



""" Code2** :
Comptage du nombre de chiffres qui se répettent dans une liste triée
Ne pas utiliser count()
L non triée = [1,4,9,3,6,3,2,5,6,3,7,8,3]
L triée     = [1,2,3,3,3,3,4,5,6,6,7,8,9]
Entrée : L=[1,2,3,3,3,3,4,5,6,6,7,8,9]
Sortie : 6 (car il y a 4 "3" + 2 "6" = 6)
"""
def count_duplicates(l):
  sorted_list = sorted(l)
  count = 0
  i = 0
  while i < len(sorted_list) - 1:
    j = i + 1
    while j < len(sorted_list) and sorted_list[j] == sorted_list[i]:
      j += 1
    if j - i > 1:
      count += (j - i - 1)
    i = j
  return count

l = [1,4,9,3,6,3,2,5,6,3,7,8,3]
print(count_duplicates(l)) # Le code sort 4 car il ne compte que le 3 et ne compte pas le 6 







