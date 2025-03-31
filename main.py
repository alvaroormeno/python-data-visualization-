import requests 
from tkinter import * 
from PIL import Image, ImageTk
from io import BytesIO

from artworkClass import ArtworkConstructor
from scroll import ScrollableFrame

# SET INITIAL PAGE TO 1
current_page = 1


def load_character_data(page):

    # FETCH DATA FROM API
    url =F'https://api.artic.edu/api/v1/artworks/search?q=monet&page={page}&limit=10&fields=title,medium_display,short_description,dimensions_detail,image_id'
    response = requests.get(url)
    jsonResponse = response.json()
    artworkResults = jsonResponse['data']

    #  Get image config URL needed to build image (api instructions)
    imageConfigUrl = jsonResponse['config']['iiif_url']

    #  Create a list of artwork instances using the ArtworkConstructor class
    artworksList = []
    for obj in artworkResults:

        title = obj['title']
        description = obj['short_description'] if obj['short_description'] else "No description available"
        medium = obj['medium_display']
        imageUrl = F"{imageConfigUrl}/{obj['image_id']}/full/843,/0/default.jpg"
        width = obj['dimensions_detail'][1]['width'] if obj['dimensions_detail'] and len(obj['dimensions_detail']) > 1  else None
        height = obj['dimensions_detail'][1]['height'] if obj['dimensions_detail'] and len(obj['dimensions_detail']) > 1  else None
        dimensions = F"{width}X{height}" if width and height else "No dimensions available"

        # Construct artwork instance 
        artwork = ArtworkConstructor(title, description, medium, dimensions, imageUrl)
        artworksList.append(artwork)

    return artworksList



# Create GUI
root = Tk()
root.title("Monet Artworks")
root.geometry("580x600")
root.resizable(0, 0)


# NAVGATION BAR SETUP
nav_frame = Frame(root)
nav_frame.pack(pady=10)

prev_button = Button(nav_frame, text="← Prev")
prev_button.pack(side=LEFT, padx=10)

page_label = Label(nav_frame, text="Page 1")
page_label.pack(side=LEFT)

next_button = Button(nav_frame, text="Next →")
next_button.pack(side=LEFT, padx=10)

# SCROLLABLE FRAME SETUP
scrollable = ScrollableFrame(root)
scrollable.pack(fill=BOTH, expand=True)



def render_page(page):
    

    global current_page
    current_page = page

    # Load character data for the current page
    characters = load_character_data(page)
    # Update the page label with current page
    page_label.config(text=f"Page {current_page}")

    # Disable/enable buttons based on the current page
    if current_page == 1:
        prev_button.config(state=DISABLED)
    else:
        prev_button.config(state=NORMAL)

    # Clear the scrollable frame before adding new items
    for widget in scrollable.scrollable_frame.winfo_children():
        widget.destroy()


    # Add items to the scrollable frame
    for char in characters:
        listItemFrame = Frame(scrollable.scrollable_frame, borderwidth=2, relief=GROOVE)

        leftFrame = Frame(listItemFrame)
        photo = ImageTk.PhotoImage(char.get_image())
        imageLabel = Label(leftFrame, image=photo)
        imageLabel.image = photo
        imageLabel.pack(fill=BOTH, expand=True)
        leftFrame.grid(row=0, column=0, padx=5, pady=10)

        rightFrame = Frame(listItemFrame)
        Label(rightFrame, text="Title: " + char.title, font=("Arial", 12, "bold"), padx=10, wraplength=300).pack(anchor="w", expand=True)
        Label(rightFrame, text="Medium: " + char.medium, font=("Arial", 12, "bold"), padx=10).pack(anchor="w", expand=True)
        Label(rightFrame, text="Dimensions: " + char.dimensions, font=("Arial", 12, "bold"), padx=10).pack(anchor="w", expand=True)
        Label(rightFrame, text="Description: " + char.description, font=("Arial", 12, "bold"), padx=10, wraplength=300, justify="left").pack(anchor="w", expand=True)
        rightFrame.grid(row=0, column=1, sticky="we")

        listItemFrame.pack(fill=X, padx=7.5)


def go_previous():
    if current_page > 1:
        render_page(current_page - 1)

def go_next():
    render_page(current_page + 1)

prev_button.config(command=go_previous)
next_button.config(command=go_next)

render_page(current_page)
root.mainloop()




