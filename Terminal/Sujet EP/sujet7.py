# EXERCICE 1
def gb_vers_entier(tab):
    somme = 0
    n = len(tab)
    for i in range(n):
        if tab[i]:
            somme += 2 ** (n - 1 - i)
    return somme


gb_vers_entier_2 = lambda tab: sum(2**(len(tab)- 1 - i) if tab[i] else 0 for i in range(len(tab)))

print(gb_vers_entier([True, False, True, False, False, True, True]))
print(gb_vers_entier_2([True, False, True, False, False, True, True]))

# EXERCICE 2

def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        j = i
        while j > 0 and valeur_insertion < tab[j - 1]:
            tab[j] = tab[j-1]
            j -= 1
        tab[j] = valeur_insertion

# Exemple d'utilisation
tab = [98, 12, 104, 23, 131, 9]
tri_insertion(tab)
print(tab)
