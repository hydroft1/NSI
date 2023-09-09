# écrivez la fonction taille() qui sera égale à la fonction len()

def taille(mot_loc):
    total = 0
    for element in mot_loc:
        total = total + 1
    return total
    
    
    
    
mot_loc="toto"
cpt=taille(mot_loc)
print("Le nombre de caractères de la chaine mot est :",cpt)


