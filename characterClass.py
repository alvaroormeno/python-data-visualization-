import os.path
import io
import requests
from PIL import Image

class CharacterConstructor:
    def __init__(self, name, gender, species, origin, status, image, numberEpisodes):
        self.name = name
        self.gender = gender
        self.species = species
        self.origin = origin
        self.status = status
        self.imageUrl = image
        self.numberEpisodes = numberEpisodes

        self.imageName = self.name.replace(" ", "_").lower() + ".png"
        self.imagePath = './ImagesCache/' + self.imageName
        self.save_image()
        

    def show_character(self):
        print(self.name, self.gender)


    def save_image(self):
        # Verify if image doesnt exist, else download image
        print(f"Image path: {self.imagePath}")

        if not os.path.exists(self.imagePath):
            response = requests.get(self.imageUrl)
            imgData = response.content

            image = Image.open(io.BytesIO(imgData))

            # Resize image
            imageResized = image.resize((200, 200), Image.Resampling.LANCZOS)
            # Save image
            imageResized.save(self.imagePath)


            print(f"Image saved as {self.imageName}")

    def get_image(self):
        return Image.open(self.imagePath)