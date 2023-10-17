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
img.show()

