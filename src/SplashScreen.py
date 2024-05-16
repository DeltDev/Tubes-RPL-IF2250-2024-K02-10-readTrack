from tkinter import *
import customtkinter as ctk
import ButtonController as BC
import LogoLoader as LL

#buat 
def create(root):
  for widget in root.winfo_children():
      widget.destroy()
  splashFrame = ctk.CTkFrame(root,
                             width=1280,
                             height = 720)
  splashFrame.pack_propagate(False)
  splashFrame.pack(padx = 10, pady = 10)
  readTrackLabel = ctk.CTkLabel(splashFrame,
                                text="readTrack v1.0",
                                font=("Segoe UI Light",36))
  readTrackLabel.pack(pady=50)
  readTrackImageLabel = ctk.CTkLabel(splashFrame, text="", image=LL.loadLogo(400,400))
  readTrackImageLabel.pack(pady=0)

  startButton = ctk.CTkButton(splashFrame,
                              text="Mulai",
                              command=lambda: BC.switchToMenu(root),
                              font=("Segoe UI Light", 20),
                              height=50,
                              width=75)
  startButton.pack(pady=50)