import requests 
from tkinter import * 
from PIL import Image, ImageTk
from io import BytesIO

from characterClass import CharacterConstructor
from scroll import ScrollableFrame


def load_character_data():
    url = 'https://rickandmortyapi.com/api/character/?page=1'
    response = requests.get(url)
    jsonResponse = response.json()

    charResults = jsonResponse['results']
    charactersList = []

    for obj in charResults:
        name = obj['name']
        gender = obj['gender']
        species = obj['species']
        origin = obj['origin']['name']
        status = obj['status']
        imageUrl = obj['image']
        numberEpisodes = len(obj['episode'])

        # # Load image from URL
        # response = requests.get(imageUrl)
        # img_data = response.content
        # img = Image.open(BytesIO(img_data))

        # Pass PIL image to character
        character = CharacterConstructor(name, gender, species, origin, status, imageUrl, numberEpisodes)
        charactersList.append(character)

    return charactersList


# Load characters
characters = load_character_data()

# Store image references so they don’t get garbage collected
photo_refs = []

# Create GUI
root = Tk()
root.title("Rick and Morty Characters")
root.geometry("500x600")
root.resizable(0, 0)
scrollable = ScrollableFrame(root)

for char in characters:
    # Main item frame
    listItemFrame = Frame(scrollable.scrollable_frame, borderwidth=2, relief=GROOVE)

    # LEFT FRAME (Image)
    leftFrame = Frame(listItemFrame)

    photo = ImageTk.PhotoImage(char.get_image())


    imageLabel = Label(leftFrame, image=photo)
    imageLabel.image = photo  # also store reference in label
    imageLabel.pack(fill=BOTH, expand=True)

    leftFrame.grid(row=0, column=0, padx=5, pady=10)

    # RIGHT FRAME (Text)
    rightFrame = Frame(listItemFrame)

    Label(rightFrame, text="Name: " + char.name, font=("Arial", 12, "bold"), padx=5).pack(anchor="w", expand=True)
    Label(rightFrame, text="Species: " + char.species, font=("Arial", 12, "bold"), padx=5).pack(anchor="w", expand=True)
    Label(rightFrame, text="Origin: " + char.origin, font=("Arial", 12, "bold"), padx=5).pack(anchor="w", expand=True)
    Label(rightFrame, text="Status: " + char.status, font=("Arial", 12, "bold"), padx=5).pack(anchor="w", expand=True)

    rightFrame.grid(row=0, column=1, sticky="we")

    # Add list item to scrollable frame
    listItemFrame.pack(fill=X, padx=7.5)

# Pack and run
scrollable.pack(fill=BOTH, expand=True)
root.mainloop()









# OLD CODE
# import requests 
# from tkinter import * 
# from PIL import Image, ImageTk
# from io import BytesIO

# from characterClass import CharacterConstructor
# from scroll import ScrollableFrame


# def load_character_data():
#     url = 'https://rickandmortyapi.com/api/character/?page=1'
#     response = requests.get(url)
#     jsonResponse = response.json()

#     charResults = jsonResponse['results']
#     charactersList = []

#     for obj in charResults:
#         name = obj['name']
#         gender = obj['gender']
#         species = obj['species']
#         origin = obj['origin']['name']
#         status = obj['status']
#         imageUrl = obj['image']
#         numberEpisodes = len(obj['episode'])

#         # # Load image from URL
#         # response = requests.get(imageUrl)
#         # img_data = response.content
#         # img = Image.open(BytesIO(img_data))

#         # Pass PIL image to character
#         character = CharacterConstructor(name, gender, species, origin, status, imageUrl, numberEpisodes)
#         charactersList.append(character)

#     return charactersList


# # Load characters
# characters = load_character_data()

# # Store image references so they don’t get garbage collected
# photo_refs = []

# # Create GUI
# root = Tk()
# root.title("Rick and Morty Characters")
# root.geometry("500x600")
# root.resizable(0, 0)
# scrollable = ScrollableFrame(root)

# for char in characters:
#     # Main item frame
#     listItemFrame = Frame(scrollable.scrollable_frame, borderwidth=2, relief=GROOVE)

#     # LEFT FRAME (Image)
#     leftFrame = Frame(listItemFrame)

#     photo = ImageTk.PhotoImage(char.get_image())


#     imageLabel = Label(leftFrame, image=photo)
#     imageLabel.image = photo  # also store reference in label
#     imageLabel.pack(fill=BOTH, expand=True)

#     leftFrame.grid(row=0, column=0, padx=5, pady=10)

#     # RIGHT FRAME (Text)
#     rightFrame = Frame(listItemFrame)

#     Label(rightFrame, text="Name: " + char.name, font=("Arial", 12, "bold"), padx=5).pack(anchor="w", expand=True)
#     Label(rightFrame, text="Species: " + char.species, font=("Arial", 12, "bold"), padx=5).pack(anchor="w", expand=True)
#     Label(rightFrame, text="Origin: " + char.origin, font=("Arial", 12, "bold"), padx=5).pack(anchor="w", expand=True)
#     Label(rightFrame, text="Status: " + char.status, font=("Arial", 12, "bold"), padx=5).pack(anchor="w", expand=True)

#     rightFrame.grid(row=0, column=1, sticky="we")

#     # Add list item to scrollable frame
#     listItemFrame.pack(fill=X, padx=7.5)

# # Pack and run
# scrollable.pack(fill=BOTH, expand=True)
# root.mainloop()