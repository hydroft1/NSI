# EXERCICE 1
def selection_enclos(animaux, num_enclos):
    return [ animal for animal in animaux if animal['enclos'] == num_enclos]
    """
    table = []
    for dico in animaux:
        if dico["enclos"] == num_enclos:
            table.append(dico)
    return table
    """
            

animaux = [ {'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2},
            {'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},
            {'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},
            {'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3},
            {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]

assert selection_enclos(animaux, 5) == [{'nom': 'Titine', 'espece': 'chat', 'age': 2, 'enclos': 5}, {'nom': 'Mirza', 'espece': 'chat', 'age': 6, 'enclos': 5}]

# EXERCICE 2
def trouver_intrus(tab, g, d):
    """Renvoie la valeur de l'intrus situÃ© entre les indices g et d 
    dans le tableau tab oÃ¹ :
    tab vÃ©rifie les conditions de l'exercice,
    g et d sont des multiples de 3."""
    if g == d:
        return tab[d] 
    else:
        nombre_de_triplets = (d - g) // 3 
        indice = g + 3 * (nombre_de_triplets // 2)
        if tab[indice] == tab[indice + 1]: 
            return trouver_intrus(tab, indice+3, d) 
        else:
            return trouver_intrus(tab, g , indice)
        
assert trouver_intrus([3, 3, 3, 9, 9, 9, 1, 1, 1, 7,
2, 2, 2, 4, 4, 4, 8, 8, 8], 0, 18) == 7