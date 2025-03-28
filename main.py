
import requests 
from tkinter import * 
from PIL import Image, ImageTk
from io import BytesIO


from characterClass import CharacterConstructor

from scroll import ScrollableFrame
# import tkinter as tk
# from tkinter import ttk


def load_character_data():
    url = 'https://rickandmortyapi.com/api/character/?page=1'
    response = requests.get(url)
    jsonResponse = response.json()

    charResults = jsonResponse['results']
    # print(jsonResponse['results'][0])


    charactersList = []
    for obj in charResults:
        name = obj['name']
        gender = obj['gender']
        species = obj['species']
        origin = obj['origin']['name']
        status = obj['status']
        imageUrl = obj['image']
        numberEpisodes = len(obj['episode'])
        # print(name)

        character = CharacterConstructor(name, gender, species, origin, status, imageUrl, numberEpisodes)

        character.show_character()

        charactersList.append(character)

    return charactersList


characters = load_character_data()



# CREATING UI
root = Tk()
root.title("Rick and Morty Characters")
root.geometry("800x600")
root.update()
root.resizable(0, 0)
scrollable = ScrollableFrame(root)


for char in characters:

    #Main Item Frame for characters
    listItemFrame = Frame(scrollable.scrollable_frame, borderwidth=2, relief=GROOVE)

    # LEFT FRAME
    leftFrame = Frame(listItemFrame)


    # Load image from URL
    response = requests.get(char.image)
    img_data = response.content
    img = Image.open(BytesIO(img_data))

    # Convert to Tkinter image
    photo = ImageTk.PhotoImage(img)


    Label(leftFrame, image=photo).pack(fill=BOTH, expand=True)

    leftFrame.grid(row=0, column=0, padx=5, pady=10)



    # RIGHT FRAME
    rightFrame = Frame(listItemFrame)
    # Name Label
    Label(rightFrame, text = "Name: " + char.name, font=("Arial", 12, "bold"),  padx=5).pack(anchor="w", expand=True)
    # Name Label
    Label(rightFrame, text = "Species: " + char.species, font=("Arial", 12, "bold"),  padx=5).pack(anchor="w", expand=True)
    # Name Label
    Label(rightFrame, text = "Origin: " + char.origin, font=("Arial", 12, "bold"),  padx=5).pack(anchor="w", expand=True)
    # Name Label
    Label(rightFrame, text = "Status: " + char.status, font=("Arial", 12, "bold"),  padx=5).pack(anchor="w", expand=True)

    # rightFrame.grid(row=0, column=1, padx=5, pady=10)

    rightFrame.grid(row=0, column=1, sticky="we")

    listItemFrame.pack(fill = X, padx = 7.5)


scrollable.pack(fill=BOTH, expand=True)
root.mainloop()