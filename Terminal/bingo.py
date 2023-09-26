class Grille:
    def __init__(self, tableau):
        self.matrice = [tableau[i:i+5] for i in range(0, 25, 5)]
        self.marques = [[False] * 5 for _ in range(5)]

    def marque(self, nombre):
        for i in range(5):
            for j in range(5):
                if self.matrice[i][j] == nombre:
                    self.marques[i][j] = True

    def est_ligne_remplie(self, indice_ligne):
        return all(self.marques[indice_ligne])

    def est_gagnante(self):
        for i in range(5):
            if self.est_ligne_remplie(i):
                return True
        
        for j in range(5):
            colonne = [self.marques[i][j] for i in range(5)]
            if all(colonne):
                return True

        diagonale_principale = [self.marques[i][i] for i in range(5)]
        diagonale_secondaire = [self.marques[i][4 - i] for i in range(5)]

        if all(diagonale_principale) or all(diagonale_secondaire):
            return True

        return False
