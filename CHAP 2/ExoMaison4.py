# transformer ce programme avec une expression booléenne

from datetime import date
aujourdhui = date.today()     #la variable aujourdhui prend pour valeur la date du jour
an_actuel = aujourdhui.year
mois_actuel = aujourdhui.month
jour_actuel = aujourdhui.day
jour_naissance = int(input("Quelle est ton jour de naissance"))
mois_naissance = int(input("Quelle est ton mois de naissance"))
an_naissance =int(input("Quelle est ton année de naissance"))



if(mois_naissance>mois_actuel) or ((mois_naissance==mois_actuel) and (jour_naissance>jour_actuel)):
    age = an_actuel-an_naissance-1      
print("Votre age est",age,"ans") # L'age ne veut pas s'afficher et la variable age n'est pas definie alors que je l'ai définie juste au dessus 




"""
if(mois_naissance>mois_actuel):
    age = an_actuel-an_naissance-1
elif(mois_naissance==mois_actuel):
    if (jour_naissance>jour_actuel):
        age = an_actuel-an_naissance-1
    else:
        age = an_actuel-an_naissance
else:
    age = an_actuel-an_naissance

print("Votre age est",age,"ans")
"""