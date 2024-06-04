# EXERCICE 1
def effectif_notes(tab):
    t = [0] * 11
    for note in tab:
        t[note] = t[note] + 1
    return t


def notes_triees(tab):
    t = []
    for i in range(tab):
        for _ in range(tab[i]):
            t.append(i)
    return t

# EXERCICE 2
