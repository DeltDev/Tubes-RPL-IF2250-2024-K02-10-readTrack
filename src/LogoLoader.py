import customtkinter as ctk
from PIL import Image

def loadLogo(width,height):
    readTrackImage = ctk.CTkImage(light_image=Image.open('../img/readTracklogo.png'),
                               dark_image=Image.open('../img/readTracklogo.png'),
                               size=(width, height))
    return readTrackImage