from tkinter import *
import customtkinter as ctk
from PIL import Image
import ButtonController as BC

def create(root):
  for widget in root.winfo_children():
      widget.destroy()
  topFrame = ctk.CTkFrame(root,
                          border_color="#247541",
                          border_width=3,
                          width=1260,
                          height = 160)
  bottomFrame = ctk.CTkFrame(root,
                            border_color="#247541",
                            border_width=3,
                            width=1260,
                            height = 580)
  
  topFrame.pack_propagate(False)
  topFrame.pack()
  bottomFrame.pack_propagate(False)
  bottomFrame.pack()
  menuLabel = ctk.CTkLabel(topFrame, text="readTrack v1.0", font=("Segoe UI Light", 24))
  menuLabel.pack(pady=20)
  backButton = ctk.CTkButton(topFrame,
                             text="Kembali",
                             command=lambda: BC.switchToSplash(root),
                             font=("Segoe UI Light", 20),
                             height=50,
                             width=75)
  backButton.pack(padx= 40)
