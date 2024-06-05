# EXERCICE 1
def tri_selection(tab):
    N = len(tab)
    for i in range(N-1):
        imin = i
        for j in range (i+1,N):
            if tab[j] < tab[imin]:
                imin = j
        if imin != i:
            tab[i], tab[imin] = tab[imin], tab[i]
            
tab = [1, 52, 6, -9, 12]
print(tri_selection(tri_selection(tab)))

# EXERCICE 2
from random import randint

def plus_ou_moins():
    nb_mystere = randint(1, 99) 
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1 

    while nb_mystere != nb_test and compteur < 10: 
        compteur = compteur + 1
        if nb_mystere > nb_test: 
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre Ã©tait ", nb_mystere) 
        print("Nombre d'essais: ", ) 
    else:
        print ("Perdu ! Le nombre Ã©tait ", nb_mystere)