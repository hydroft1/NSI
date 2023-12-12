from PIL import Image, ImageDraw
import transgeo as tg


class Segment:
    def __init__(self, pt1, pt2):
        self.pt1 = pt1
        self.pt2 = pt2

    def rotation(self, angle, pt):
        pt1 = tg.rotation(self.pt1, angle, pt)
        pt2 = tg.rotation(self.pt2, angle, pt)
        return Segment(pt1, pt2)

    def trace(self, ctx, **kwargs):
        ctx.line([self.pt1, self.pt2], **kwargs)
        pt3 = tg.homothetie(self.pt1, self.pt2, 3)
        pt4 = tg.homothetie(self.pt2, self.pt1, 3)
        ctx.line([self.pt1, pt3], width= 10, fill="black")
        ctx.line([self.pt2, pt4], width= 10, fill="black")

pi = "31415926535897932384626433832795028841971693993751"
angle_deg = -1.5
W = H = 800
img = Image.new("RGB", (W, H), "black")
calque = ImageDraw.Draw(img)
marge = 50

s = Segment((W//2, H//2), (W//2, H//2 + 100))
s.trace(calque, width=4, fill= "white")

for i in range(len(pi)):
    if i % 2 == 0:
        pt = s.pt1
        ang = angle_deg * int(pi[i])
    else:
        pt = s.pt2
        ang = - angle_deg * int(pi[i])
    s = s.rotation(ang, pt)
    s.trace(calque)

img.save(f"pi_piquant_{abs(angle_deg)}.jpg")
