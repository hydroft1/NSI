from random import randint
nb_ordi=randint(1,100)
print(nb_ordi)

while (nb_ordi != nb_utilisateur):
    if (nb_ordi>nb_utilisateur):
        print("c'est plus")
    else:
         print ("c'est moins")
    nb_utilisateur = int(input("choisis un nombre,tu as tu as choisis le ..."))
print("bravo ")


