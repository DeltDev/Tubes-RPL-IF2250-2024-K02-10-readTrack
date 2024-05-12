from Buku import *
from tkinter import *
import customtkinter as ctk
from PIL import Image
import ButtonController as BC
import LogoLoader as LL

LoadState.loadBuku()
def createInginDibacaPage(root,color):
    buttonAddBuku = ctk.CTkButton(root,
                                  width = 200,
                                  height=40,
                                  text="Tambah Buku Baru",
                                  font=("Segoe UI Light",20))
    buttonAddBuku.pack()
    for temp in DaftarBukuInginDibaca.listBukuInginDibaca:
        bookFrame = ctk.CTkFrame(root,
                                 width=800,
                                 height=200,
                                 border_color=color,
                                 border_width=3)
        bookFrame.pack(pady = 20)
        bookTitleLabel = ctk.CTkLabel(bookFrame, 
                                      text=temp.judul, 
                                      font=("Segoe UI Light", 24))
        bookTitleLabel.place(x=20,y=20)
        bookWriterLabel = ctk.CTkLabel(bookFrame, 
                                      text="Penulis: "+temp.penulis, 
                                      font=("Segoe UI Light", 20))
        bookWriterLabel.place(x=20,y=60)
        bookPublisherLabel =ctk.CTkLabel(bookFrame, 
                                      text="Penerbit: "+temp.penerbit, 
                                      font=("Segoe UI Light", 20))
        bookPublisherLabel.place(x=20,y=90)
        bookTotalPageLabel =ctk.CTkLabel(bookFrame, 
                                      text="Jumlah halaman: "+str(temp.totalHalaman)+" halaman", 
                                      font=("Segoe UI Light", 20))
        bookTotalPageLabel.place(x=20,y=120)

        #tombol untuk memindahkan buku ke list buku yang sedang dibaca
        mulaiBacaButton = ctk.CTkButton(bookFrame,
                                        width = 150,
                                        height=40,
                                        text="Mulai Baca!",
                                        font=("Segoe UI Light",20))
        mulaiBacaButton.place(x=620,y=140)

        #tombol untuk menghapus buku yang ingin dibaca
        hapusBukuButton = ctk.CTkButton(bookFrame,
                                        width = 150,
                                        height=40,
                                        text="Hapus Buku",
                                        font=("Segoe UI Light",20),
                                        fg_color="#B32B3D",
                                        hover_color="#821F2C",
                                        command=lambda bookFrame=bookFrame,title=temp.judul: hapusBukuInginDibacaPrompt(root,bookFrame,title))
        hapusBukuButton.place(x= 450, y =140)
        
def hapusBukuInginDibacaPrompt(root,bookFrame,title):
    print(title)
    for widget in bookFrame.winfo_children():
      widget.destroy()
    promptLabel1 = ctk.CTkLabel(bookFrame,
                                text="Apakah Anda yakin untuk menghapus buku ini dari daftar buku yang ingin dibaca?",
                                font=("Segoe UI Light", 20))
    promptLabel1.place(x=50,y=10)

    promptLabel2 = ctk.CTkLabel(bookFrame,
                                text="PERINGATAN: TINDAKAN INI BERSIFAT PERMANEN DAN ANDA \nTIDAK AKAN BISA MENGEMBALIKAN BUKU INI SETELAH DIHAPUS!",
                                font=("Segoe UI Bold", 20),
                                text_color="#B32B3D")
    promptLabel2.place(x=70,y=50)

    yesButton = ctk.CTkButton(bookFrame,
                              width = 150,
                              height=40,
                              text="Ya",
                              font=("Segoe UI Light",20),
                              fg_color="#B32B3D",
                              hover_color="#821F2C")
    yesButton.place(x=200, y =140)

    noButton = ctk.CTkButton(bookFrame,
                              width = 150,
                              height=40,
                              text="Tidak",
                              font=("Segoe UI Light",20))
    noButton.place(x=450, y =140)