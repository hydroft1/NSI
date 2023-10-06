class Bingo : 
    def __init__(self, tab):
        self.matrices = []
        for i in range(5):
            ligne = []
            for j in range(5):
                ligne.append([tab[5*i + j], 0])
            self.matrices.append(ligne)
    
    def __str__(self):
        stg = ""
        for i in range(5):
            for j in range(5):
                stg += str(self.matrices[i][j][0]) + " "
            stg += "\n"
        return stg[:-1]
    
    def __getitem__(self, indice):
        return self.matrices[indice]


def lecture_grille(nom_ficher):
    """
    lit un fichier de grille de bingo
    1 une ligne fichier = 1 ligne bingo
    les nombres sont espacés par des espaces
    """
    
    tableau  = []
    with open(nom_ficher) as fh:
        for ligne in fh:
            ligne = ligne.rstrip()
            tb = ligne.split()
            tb = [int(c) for c in tb]
            for elt in tb:
                tableau.append(elt)
            
    return tableau


if __name__ == '__main__':
   la_grille = lecture_grille("grille.dat")
   print(la_grille)  
   
    #b = Bingo(T)
    #print(b)
    #print(b[3][4][0])