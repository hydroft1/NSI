"""
# EXERCICE 3
import transgeo as tg
from PIL import Image, ImageDraw

def sierpinski_rec(profondeur, A, B):
    C = tg.rotation60(B, A)
    # condition d'arrêt
    if profondeur == 0:
        CTX.polygon([A, B, C], fill="white")
        return 
    #
    # appels récursifs
    B_prime = tg.milieu(A, B)
    I = tg.milieu(A, C)
    I_prime = tg.milieu(B, C)
    sierpinski_rec(profondeur - 1, A, B_prime)
    sierpinski_rec(profondeur - 1, B_prime, B)
    sierpinski_rec(profondeur - 1, I, I_prime)
    

W = 2000
H = W
img = Image.new("RGB", (W, H))
CTX = ImageDraw.Draw(img)
#
sierpinski_rec(13, (0, 0), (W - 1, 0))
img.save("sierpinski.png")
img.show()"""

# exercice 1

def est_palin_mot(mot):
    if  len(mot) <= 1: return True
    #
    if mot[0] == mot[len(mot)-1]: return est_palin_mot(mot[1:len(mot)-1])
    else:
        return False
    
def est_palin_mot_v2(mot):
    n = len(mot)  
    if n <= 1: return True
    #
    return mot[0] == mot[n - 1] and est_palin_mot_v2(mot[1:n - 1])
    
def _est_palin_mot_v3(mot, indice):
    n = len(mot)
    if indice == n // 2: return True
    return mot[0] == mot[n - 1 - indice] and _est_palin_mot_v3(mot, indice + 1)

def est_palindrome(mot):
    """ Fonction D'interface """
    return _est_palin_mot_v3(mot, 0)