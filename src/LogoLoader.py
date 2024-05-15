from tkinter import *
import customtkinter as ctk
from PIL import Image

def loadLogo(width,height):
    readTrackImage = ctk.CTkImage(light_image=Image.open('images/readTracklogo.png'),
                               dark_image=Image.open('images/readTracklogo.png'),
                               size=(width, height))
    return readTrackImage