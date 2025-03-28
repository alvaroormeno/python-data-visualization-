class CharacterConstructor:
    def __init__(self, name, gender, species, origin, status, image, numberEpisodes):
        self.name = name
        self.gender = gender
        self.species = species
        self.origin = origin
        self.status = status
        self.image = image
        self.numberEpisodes = numberEpisodes

    def show_character(self):
        print(self.name, self.gender)