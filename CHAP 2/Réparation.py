
# Code 2
"""
nb1=int(input("Donner le 1er nombre"))
nb2=int(input("Donner le 2eme nombre"))
resultat = nb1+nb2
nombre_trouvé=int(input("donner l'addition de ces 2 nombres de tête"))
while (nombre_trouvé!=resultat):
    print("essais encore")
    nombre_trouvé=int(input("donner l'addition de ces 2 nombres de tête"))
print("bravo")
"""



# Code 2
"""
nb1=int(input("Donner le 1er nombre : "))
nb2=int(input("Donner le 2eme nombre : "))
resultat = nb1+nb2
nombre_trouvé = int(input("Donner la somme de "+str(nb1)+" + "+str(nb2)+"="))
while(resultat!=nombre_trouvé):
    if (d_rslt!=(nb1+nb2)):
        print("Essais encore")
    nombre_trouvé = int(input("Donner la somme de "+str(nb1)+" + "+str(nb2)+"="))
print("bravo !")
"""




#Code3
"""
nb1=int(input("Donner le 1er nombre"))
nb2=int(input("Donner le 2eme nombre"))
print("Donner le resultat de",nb1,"+",nb2,)
rep=int(input("reponse:"))
resultat=nb1+nb2
nb_essais=1
while (rep!=resultat) and nb_essais!=5:
    print("essaye encore !")
    print("Donner le resultat de",nb1,"+",nb2,)
    rep=int(input("reponse:"))
    resultat=nb1+nb2
    nb_essais=nb_essais+1
if rep==resultat :
    print("Bravo, tu as réussi en",nb_essais,"essais !")
else:
    print("Dommage, les 5 essais sont passés")
"""


#Code3
"""
nb1c3=int(input("Donner le 1er nombre: "))
nb2c3=int(input("Donner le 2eme nombre: "))
nbc3_somme_ut=int(input("Donner la somme des deux: "))
essais=1
while essais<5 and (nbc3_somme_ut!=nb1c3+nb2c3):
    print("essayer a nouveau")
    nbc3_somme_ut=int(input("Donner la somme des deux: "))
    essais=essais+1
if essais<5 :
    print("bravo tu as reussi en",essais,"essais")
else:
    print("dommage les",essais,"essais sont passés")

"""



#Code3
"""
nb1=int(input("Donner le 1er nombre"))
nb2=int(input("Donner le 2eme nombre"))
nb3=nb1+nb2
nb4=int(input("Quel doit être l'addition des 2 nombres ?"))
x1=1
x2=5
while nb3!=nb4 and x1<x2:
    print("Essais encore")
    nb4=int(input("Quel doit être l'addition des 2 nombres ?"))
    x1=x1+1

if x1<x2 :
    print("bravo tu as reussi en",x1,"essais")

else:
    print("Dommage, les 5 essais sont passés")

"""






#Code3
"""  
nb1=int(input("Donner le 1er nombre..."))
nb2=int(input("Donner le 2eme nombre..."))
resultat=nb1+nb2
nb_essais=1
nb_essais_max=3
resultat_joueur=int(input("Doner le resultat de l'addition des 2 nombres ..."))
while (resultat_joueur!=resultat) and (nb_essais<nb_essais_max):
    print("Mauvaise réponse, retente ta chance")
    resultat_joueur=int(input("Doner le resultat de l'addition des 2 nombres ..."))
    nb_essais= nb_essais+1

if (resultat_joueur==resultat):
    print("Bravo, tu as reussi en",nb_essais,"essais")
else:
    print("Dommage, les 3 essais sont passés")   
""" 
    
    
    
    
    
    
    
    

#Code3

"""
nb1=int(input("Donner le premier nombre: "))
nb2=int(input("Donner le second nombre: "))
solution=int(input("Donner l'addition de ces 2 nombres de tête: "))
essais=0
essais_max=5
while(solution!=nb1+nb2) and essais<essais_max:
    print("Essais encore")
    solution=int(input("Essayez à nouveau: "))
    essais=essais+1

if(essais<essais_max):
    print("Bravo tu as réussi en", essais, "essais !")
else:
    print("Dommage, les", essais_max, "essais sont passés")
"""
