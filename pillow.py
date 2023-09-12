from PIL import Image, ImageDraw

class Croix:
    def __init__(self, xy, d):
        self.x, self.y = xy 
        self.dim = d
    def trace(self, cntx):
        d = self.dim / 2
        cntx.line([(self.x - d, self.y - d), 
                  (self.x + d , self.y + d )])
        cntx.line([(self.x + d, self.y - d),
                   (self.x - d, self.y + d)])
        
img = Image.new("RGB", (800, 800))
ctx = ImageDraw.Draw(img)
c = Croix((400, 400), 100)
c.trace(ctx)
img.save("test_pil.jpg")
