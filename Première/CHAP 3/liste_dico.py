# CODE 1

def creationLivre():
    dicoLivre={}
    dicoLivre["Auteur"]= input ("Entrez l'auteur du Livre :")
    dicoLivre["Titre"]= input ("Entrez le Titre du Livre :")
    dicoLivre["Pages"]= input ("Entrez le nombre de Pages du Livre :")
    dicoLivre["Editeur"]= input ("Entrez l'Editeur du Livre :")
    return dicoLivre

dicoLivre = creationLivre()
print (dicoLivre)

# CODE 2

def ajoutLivre(dicoLivre,listeBibliotheque):
    
