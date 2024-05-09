from tkinter import *
import customtkinter as ctk
from PIL import Image
#setup warna background

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

#root
root = ctk.CTk()
root.title('readTrack - Aplikasi Tracker Buku')
root.geometry('1280x720')
root.iconbitmap("images/readTracklogo.ico")
#tombol untuk membuka aplikasi
def hello(): #ini hanya fungsi placeholder, buat ganti scene ke menu utama
    print("HELLO")
#gambar logo
readTrackImage = ctk.CTkImage(light_image=Image.open('images/readTracklogo.png'),
                              dark_image=Image.open('images/readTracklogo.png'),
                              size=(400,400))
#nama aplikasi
readTrackLabel = ctk.CTkLabel(root,
                              text="readTrack",
                              font=("Segoe UI Light",36))
readTrackLabel.pack(pady=50)
#display gambar
readTrackImageLabel = ctk.CTkLabel(root,text="",image=readTrackImage)
readTrackImageLabel.pack(pady=0)
#tombol untuk berpindah scene
startButton = ctk.CTkButton(root, 
                            text="Mulai",
                            command=hello,
                            font =("Segoe UI Light", 20),
                            height=50,
                            width = 75)
startButton.pack(pady=50)
root.mainloop()