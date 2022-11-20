# CODE 1
"""
def moyenne(L_notes_loc):
    somme_loc=0
    for i in range (len(L_notes_loc)):
        somme_loc=L_notes_loc[i]+somme_loc
    moy_loc=somme_loc/len(L_notes_loc)       
    return(moy_loc)
L_notes_loc=[11.5,10,14.5,13,7,16,9]
moy_loc=moyenne(L_notes_loc)
print("la moyenne est de :",moy_loc)
"""

# CODE 2
def moyenne(L_notes_loc):
    somme_loc=0
    for i in range (len(L_notes_loc)):
        somme_loc=L_notes_loc[i]+somme_loc
    moy_loc=somme_loc/len(L_notes_loc)       
    return(moy_loc)
 
def notes_plus_1(L_notes_loc):
    n = moyenne(L_notes_loc)
    if (moyenne(L_notes_loc))<12:
        L_notes_loc[i]=L_notes_loc[i]+1
    return(L_notes_loc)
