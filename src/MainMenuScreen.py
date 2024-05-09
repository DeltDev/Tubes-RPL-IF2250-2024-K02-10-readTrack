from tkinter import *
import customtkinter as ctk
from PIL import Image
import ButtonController as BC
import LogoLoader as LL
def create(root):
  for widget in root.winfo_children():
      widget.destroy()
  masterFrame = ctk.CTkFrame(root,
                             width=1280,
                             height=720)
  topFrame = ctk.CTkFrame(masterFrame,
                          width=1280,
                          height = 160)
  bottomFrame = ctk.CTkFrame(masterFrame,
                            width=1280,
                            height = 580)
  logoFrame = ctk.CTkFrame(topFrame,
                            width = 130,
                            height = 130)
  bookSelectionFrame = ctk.CTkFrame(bottomFrame,
                                    width = 130,
                                    height = 550)
  bookListFrame = ctk.CTkFrame(bottomFrame,
                               width = 1085,
                               height = 550)
  masterFrame.pack()
  topFrame.pack_propagate(False)
  topFrame.pack()
  bottomFrame.pack_propagate(False)
  bottomFrame.pack()
  logoFrame.pack_propagate(False)
  logoFrame.pack(side=LEFT,padx=15)
  bookSelectionFrame.pack_propagate(False)
  bookSelectionFrame.pack(side=LEFT,padx=15)
  bookListFrame.pack_propagate(False)
  bookListFrame.pack(side=LEFT)
  readTrackImageLabel = ctk.CTkLabel(logoFrame, text="", image=LL.loadLogo(175,175), width=200, height= 200)
  readTrackImageLabel.pack()
  readTrackImageLabel.pack_propagate(False)
  menuLabel = ctk.CTkLabel(topFrame, text="Daftar Buku", font=("Segoe UI Light", 48))
  menuLabel.pack(pady=20)
  menuLabel2 = ctk.CTkLabel(topFrame, text="readTrack v1.0", font=("Segoe UI Light", 24))
  menuLabel2.pack(side=TOP)
  backButton = ctk.CTkButton(bookSelectionFrame,
                             text="Kembali",
                             command=lambda: BC.switchToSplash(root),
                             font=("Segoe UI Light", 20),
                             height=50,
                             width=75)
  backButton.pack_propagate()
  backButton.pack(side=BOTTOM,pady=15)
