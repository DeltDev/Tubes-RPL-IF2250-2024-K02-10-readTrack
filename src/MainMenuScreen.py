from tkinter import *
import customtkinter as ctk
from PIL import Image
import ButtonController as BC

def create(root):
  for widget in root.winfo_children():
      widget.destroy()
  menuLabel = ctk.CTkLabel(root, text="readTrack", font=("Segoe UI Light", 24))
  menuLabel.pack(pady=20)
  backButton = ctk.CTkButton(root,
                             text="Kembali",
                             command=lambda: BC.switchToSplash(root),
                             font=("Segoe UI Light", 20),
                             height=50,
                             width=75)
  backButton.pack(padx= 40)
