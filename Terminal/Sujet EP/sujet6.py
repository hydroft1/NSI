# EXERCICE 1
def verifie(tab):
    if len(tab) < 2:
        return True
    for i in range(1, len(tab)):
        if tab[i] < tab[i - 1]:
            return False
    return True

# EXERCICE 2
def depouille(urne):
    '''prend en paramÃ¨tre une liste de suffrages et renvoie un 
    dictionnaire avec le nombre de voix pour chaque candidat'''
    resultat = {} 
    for bulletin in urne:
        if bulletin in resultat: 
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueurs(election):
    '''prend en paramÃ¨tre un dictionnaire non vide avec le nombre de voix
    pour chaque candidat et renvoie la liste des vainqueurs'''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax : 
            nmax = election[candidat]
    liste_finale = [ nom for nom in election if election[nom] == nmax] 
    return liste_finale 