# EXERCICE 1
T1 = [n for n in range(201) if n%2 == 0]
T4 = [n for n in T1 if n % 7 == 0 and n % 4 != 0]
T5 = []

# EXERCICE 2
def vers_dico(tabch, tabint):
    dico = {}
    for key, value in zip(tabch, tabint):
        dico[key] = value
    return dico
 
      

# EXERCICE 3    
def vers_liste(dico):
    liste = []
    for key, value in dico.items():
        liste.extend([key] * value)
    return liste


# EXERCICE 4
def dernier_ind(tab, elt):
    n = len(tab)
    trouve = False
    i = n - 1
    while i >= 0 and not trouve:
        trouve = elt == tab[i]
        i = i - 1
    if trouve:
        return i + 1
    else:
        return False


assert dernier_ind([1, 2, 3, 1], 1) == 3

# EXERCICE 5
