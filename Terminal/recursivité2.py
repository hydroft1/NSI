import Terminal.transgeo as tg
from PIL import Image, ImageDraw

def vk(profondeur, A, B):
    if profondeur == 0: CTX.line([A, B]); return
    #
    C = tg.homothetie(B, A, 1/3)
    E = tg.homothetie(B, A, 2/3)
    D = tg.rotation60(E, C)
    vk(profondeur - 1, A, C)
    vk(profondeur - 1, C, D)
    vk(profondeur - 1, D, E)
    vk(profondeur - 1, E, B)
   
    
img = Image.new("RGB", (800, 300))
CTX = ImageDraw.Draw(img)

vk(3, (0,0), (799, 0))
img.save("vk.png")
img.show()
