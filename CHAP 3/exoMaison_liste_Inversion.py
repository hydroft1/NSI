# Ecrivez un programme qui inverse les éléments d'une liste L1 dans une nouvelle liste L2
# vous n'utiliserez pas la méthode reverse().
# Exemple :
# Entrée : L1 = [5,6,7,8,9]
# Sortie : L2 = [9,8,7,6,5]
""""
L1=[5,6,7,8,9]
L2=[]
for i in range(len(L1)):
    L2.append(L1[-i-1])
print(L2)
"""
# Ecrivez un programme qui inverse les éléments d'une liste L (sans utiliser une nouvelle liste).
# vous n'utiliserez pas la méthode reverse().
# Exemple :
# Entrée : L = [5,6,7,8,9]
# Sortie : L = [9,8,7,6,5]
"""
L=[5,6,7,8,9]
print(list(reversed(L)))
"""