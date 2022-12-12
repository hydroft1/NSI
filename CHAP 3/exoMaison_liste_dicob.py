# Nouvelle règle pour avoir 1/1 sur les exos maison : réussir au moins un code demandé car il y aura à chaque fois un code facile à faire

# Code1* : créez D_match_1={"1:"Samira",2:"Léa",3:"Lucie"} à partir L_match_1=["Samira","Léa","Lucie"]



L_match_1=["Samira","Léa","Lucie"]
D_match_1={}

"""
def ajouterEleve(D_match_1s,cle,nom):
    if cle in D_match_1.keys():
        print("clé déjà présente")
    else:
        D_match_1[cle] = nom
    return D_match_1

D_match_1 = ajouterEleve(D_match_1,"1","Samira")
D_match_1 = ajouterEleve(D_match_1,"2","Léa")
D_match_1 = ajouterEleve(D_match_1,"3","Lucie")
print (D_match_1)

"""

# Code2** : créez D_match_1={"joueuse1":"Samira","Joueuse2":"Léa","Joueuse3":"Lucie"} à partir L_match_1=["Samira","Léa","Lucie"]


L_match_1=["Samira","Léa","Lucie"]
D_match_1={}


def ajouterEleve(D_match_1s,cle,nom):
    if cle in D_match_1.keys():
        print("clé déjà présente")
    else:
        D_match_1[cle] = nom
    return D_match_1

D_match_1 = ajouterEleve(D_match_1,"Joueuse 1","Samira")
D_match_1 = ajouterEleve(D_match_1,"Joueuse 2","Léa")
D_match_1 = ajouterEleve(D_match_1,"Joueuse 3","Lucie")
print (D_match_1)