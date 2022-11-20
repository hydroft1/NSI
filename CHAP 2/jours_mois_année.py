# Réalisez un programme qui donne le nombre de jours de votre mois de naissance
# Le programme doit fonctionner quelque soit le mois de naissance

mois_naissance=int(input("Quel est votre mois de naissance ? "))

if(mois_naissance==2):
    nb_jours=28
elif(mois_naissance%2==0):
    nb_jours=30
elif(mois_naissance%2==1):
    nb_jours=31

print("Vous avez",nb_jours,"jours dans votre mois")

# réduisez le nombre de lignes en utilisant l'opérateur mathématique % :
# Si (mois_naissance%2==1) alors le mois_naissance est impair
# Si (mois_naissance%2==0) alors le mois_naissance est pair