# EXERCIE 1
def taille(arbre, lettre):
    if lettre == '':
        return 0
    taille_gauche = taille(arbre, arbre[lettre][0]) if arbre[lettre][0] else 0
    taille_droite = taille(arbre, arbre[lettre][1]) if arbre[lettre][1] else 0
    return 1 + taille_gauche + taille_droite



# Exemple d'utilisation
a = {
    'F': ['B', 'G'], 
    'B': ['A', 'D'], 
    'A': ['', ''], 
    'D': ['C', 'E'], 
    'C': ['', ''], 
    'E': ['', ''], 
    'G': ['', 'I'], 
    'I': ['', 'H'], 
    'H': ['', '']
}

print(taille(a, 'F'))  # Devrait afficher 9
print(taille(a, 'B'))  # Devrait afficher 5
print(taille(a, 'I'))  # Devrait afficher 2

# EXERCICE 2
def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i]
    tab[i] = tab[j] 
    tab[j] = temp 

def tri_selection(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri par sélection.
    >>> tab = [41, 55, 21, 18, 12, 6, 25]
    >>> tri_selection(tab)
    >>> tab
    [6, 12, 18, 21, 25, 41, 55]
    '''
    N = len(tab)
    for k in range(N - 1): 
        imin = k
        for i in range(k + 1, N): 
            if tab[i] < tab[imin]: 
                imin = i
        echange(tab, k, imin) 
        
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()