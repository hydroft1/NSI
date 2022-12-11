# CODE 1 

dicoEleves = {"e2022001" : "Sophie",
    "e2022002" : "Noé",
    "e2022003" : "Léa",
    "e2022004" : "Alex",
    "e2022005" : "Manon"
}
print (dicoEleves)

# CODE 2

def ajouterEleve(dicoEleves,cle,nom):
    if cle in dicoEleves.keys():
        print("clé déjà présente")
    else:
        dicoEleves[cle] = nom
    return dicoEleves



dicoEleves = ajouterEleve(dicoEleves,"e2022006","Louis")
dicoEleves = ajouterEleve(dicoEleves,"e2022007","Manon")
dicoEleves = ajouterEleve(dicoEleves,"e2022007","Samira")
print (dicoEleves)


# CODE 3 

def modifierEleve(dicoEleves,cle,nom):
    if cle in dicoEleves.keys():
        dicoEleves[cle]= "Alexandre"
    else:
        print ("la clé n'est pas présente")
    return dicoEleves

dicoEleves = modifierEleve(dicoEleves,"e2022004","Alexandre")
dicoEleves = modifierEleve(dicoEleves,"e2022009","TOTO")
print (dicoEleves)

# CODE 4 

def supprimerEleve(dicoEleves,cle):
    if cle in dicoEleves.keys():
        print ("l'élève supprimé est :", dicoEleves[cle])
        del dicoEleves[cle]
       
    else:
        print ("pas d'élève associé à la clé")
    return dicoEleves
    

dicoEleves = supprimerEleve(dicoEleves,"e2022002",)
dicoEleves = supprimerEleve(dicoEleves,"e2022009",)
print (dicoEleves)


# CODE 5 

def afficherCle(dicoEleves,nom):
    
    return