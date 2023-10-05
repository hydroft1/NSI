from PIL import Image, ImageDraw
import random

class MosaicGenerator:
    def __init__(self, image_path, output_path, mosaic_size=20, num_colors=5):
        self.image_path = image_path
        self.output_path = output_path
        self.mosaic_size = mosaic_size
        self.num_colors = num_colors

    def generate_mosaic(self):
        # Ouvrir l'image source
        image = Image.open(self.image_path)

        # Créer un nouvel objet Image pour la mosaïque
        mosaic = Image.new('RGB', image.size)

        # Créer un objet Draw pour dessiner sur la mosaïque
        draw = ImageDraw.Draw(mosaic)

        # Diviser l'image en mosaïques et les remplir avec des couleurs aléatoires
        for x in range(0, image.width, self.mosaic_size):
            for y in range(0, image.height, self.mosaic_size):
                # Sélectionner une couleur aléatoire
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                # Remplir la mosaïque avec la couleur aléatoire
                draw.rectangle([x, y, x + self.mosaic_size, y + self.mosaic_size], fill=color)

        # Enregistrement de la mosaïque générée
        mosaic.save(self.output_path)
        print(f"Mosaïque enregistrée sous {self.output_path}")

# Exemple d'utilisation de la classe MosaicGenerator
if __name__ == "__main__":
    image_path = "votre_image.jpg"  # Remplacez par le chemin de votre image source
    output_path = "mosaique.jpg"   # Le chemin où vous souhaitez enregistrer la mosaïque
    mosaic_size = 20               # Taille de chaque mosaïque
    num_colors = 5                # Nombre de couleurs aléatoires

    generator = MosaicGenerator(image_path, output_path, mosaic_size, num_colors)
    generator.generate_mosaic()
