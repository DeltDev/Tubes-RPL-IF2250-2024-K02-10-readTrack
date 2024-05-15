from tkinter import *
import customtkinter as ctk
import SplashScreen as ss
#setup customtkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

#setup root
root = ctk.CTk()
root.resizable(False, False)
root.title('readTrack - Aplikasi Tracker Buku')
root.geometry('1300x740')
root.iconbitmap("images/readTracklogo.ico")

#buka 
ss.create(root)

root.mainloop()
