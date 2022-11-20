"""
Coder un programme réalisant la multiplication de 2 entiers n1 et n2
Ne pas utiliser les opérateurs : *, / et abs()
Aide : 3x4=3+3+3+3
Exemple :
Si n1=3 et n2=4 --> résulat=12
Si n1=3 et n2=-4 --> résulat=-12
Si n1=-3 et n2=4 --> résulat=-12
Si n1=-3 et n2=-4 --> résulat=12
"""



n1=float(input("Donnez le premier nombre de la multiplication :"))
n2=float(input("Donnez le second  nombre de la multiplication :"))


total=0             # NE MARCHE PAS QUAND N2 EST UN NOMBRE NEGATIF   ET QUAND N1 ET N2 SONT  NEGATIF
for i in range (int(n2)):
    total =total+n1
print (total)