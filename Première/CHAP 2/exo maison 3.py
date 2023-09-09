# Completez le programme suivant de tel sorte que :
# Si nb_a_conv=nb_conv alors le programme affichera "Bravo".
# Sinon le programme demandera d'entrer un nouveau résultat de la conversion.
# Le programme se terminera lorsque l'utilisateur aura rentré le bon résultat de la conversion.
# Exemple si nb_a_conv=1001 et vous rentrez nb_conv=12, il faudra recommencer car il faut nb_conv=9.
# Aide : int("101010",2) donne la conversion en base 10 de (101010)2.

"""print("Entrez un nombre en base 2 à convertir vers la base 10 : ")
nb_a_conv=input()
print("Entrez le résultat de cette conversion : ")
nb_conv=int(input())
nb_conv==int(nb_a_conv,2)
while (nb_conv!=int(nb_a_conv,2)):
    print("Recommencez")
    print("Entrez le résultat de cette conversion : ")
    nb_conv=int(input())
print("Bravo")
"""
# Completez le programme précédent de tel sorte que :
# Même fonctionnement mais on choisira entre la base 2 ou la base 16 le nombre à convertir vers la base 10.
# Aide : int("2A",16) donne la conversion en base 10 de (2A)16.

print("Choissez la base 2 ou 16 : ")
base=int(input())
if (base==2):
    print("Entrez un nombre en base 2 à convertir vers la base 10 : ")
    nb_a_conv=input()
    print("Entrez le résultat de cette conversion : ")
    nb_conv=int(input())
    nb_conv==int(nb_a_conv,2)
    while (nb_conv!=int(nb_a_conv,2)):
        print("Recommencez")
        print("Entrez le résultat de cette conversion : ")
        nb_conv=int(input())
elif (base==16):
    print("Entrez un nombre en base 16 à convertir vers la base 10 : ")
    nb_a_conv=input()
    print("Entrez le résultat de cette conversion : ")
    nb_conv=int(input())
    nb_conv==int(nb_a_conv,16)
    while (nb_conv!=int(nb_a_conv,16)):
        print("Recommencez")
        print("Entrez le résultat de cette conversion : ")
        nb_conv=int(input())
print("Bravo")