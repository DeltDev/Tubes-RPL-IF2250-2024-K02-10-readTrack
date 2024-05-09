from tkinter import *
import customtkinter as ctk
from PIL import Image
import ButtonController as BC
#setup gambar buat splash screen
readTrackImage = ctk.CTkImage(light_image=Image.open('images/readTracklogo.png'),
                               dark_image=Image.open('images/readTracklogo.png'),
                               size=(400, 400))
#buat 
def create(root):
  for widget in root.winfo_children():
      widget.destroy()
  readTrackLabel = ctk.CTkLabel(root,
                                text="readTrack",
                                font=("Segoe UI Light",36))
  readTrackLabel.pack(pady=50)
  readTrackImageLabel = ctk.CTkLabel(root, text="", image=readTrackImage)
  readTrackImageLabel.pack(pady=0)

  startButton = ctk.CTkButton(root,
                              text="Mulai",
                              command=lambda: BC.switchToMenu(root),
                              font=("Segoe UI Light", 20),
                              height=50,
                              width=75)
  startButton.pack(pady=50)