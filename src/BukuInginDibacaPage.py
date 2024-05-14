from Buku import *
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image
import ButtonController as BC
import LogoLoader as LL
from datetime import datetime

LoadState.loadBuku()
def createInginDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton):
    #tombol untuk menambah buku baru
    buttonAddBuku = ctk.CTkButton(root,
                                  width = 200,
                                  height=40,
                                  text="Tambah Buku Baru",
                                  font=("Segoe UI Light",20),
                                  command=lambda root=root,indicatorArr=indicatorArr,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: tambahBukuPrompt(root,indicatorArr,indicator, color, defaultColor, buttonArr, currentButton))
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

        #tombol untuk memindahkan buku yang ingin dibaca ke list buku yang sedang dibaca
        mulaiBacaButton = ctk.CTkButton(bookFrame,
                                        width = 150,
                                        height=40,
                                        text="Mulai Baca!",
                                        font=("Segoe UI Light",20),
                                        command=lambda root=root,indicatorArr=indicatorArr,bookFrame=bookFrame,title=temp.judul,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: mulaiBacaPrompt(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title))
        mulaiBacaButton.place(x=620,y=140)

        #tombol untuk menghapus buku yang ingin dibaca
        hapusBukuButton = ctk.CTkButton(bookFrame,
                                        width = 150,
                                        height=40,
                                        text="Hapus Buku",
                                        font=("Segoe UI Light",20),
                                        fg_color="#B32B3D",
                                        hover_color="#821F2C",
                                        command=lambda root=root,indicatorArr=indicatorArr,bookFrame=bookFrame,title=temp.judul,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: hapusBukuInginDibacaPrompt(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title))
        hapusBukuButton.place(x= 450, y =140)
        
def hapusBukuInginDibacaPrompt(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title):
    # print(title)
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
                              hover_color="#821F2C",
                              command= lambda root=root,indicatorArr=indicatorArr,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton,title=title:deleteBuku(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,title))
    yesButton.place(x=200, y =140)

    noButton = ctk.CTkButton(bookFrame,
                              width = 150,
                              height=40,
                              text="Tidak",
                              font=("Segoe UI Light",20),
                              command=lambda root=root,indicatorArr=indicatorArr,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: BC.inginDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton))
    noButton.place(x=450, y =140)

def mulaiBacaPrompt(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title):
    print(title)
    for widget in bookFrame.winfo_children():
      widget.destroy()
    promptLabel1 = ctk.CTkLabel(bookFrame,
                                text="Apakah Anda ingin memulai membaca buku ini?",
                                font=("Segoe UI Light", 20))
    promptLabel1.place(x=200,y=10)

    #command untuk memindahkan buku yang ingin dibaca ke buku yang sedang dibaca
    yesButton = ctk.CTkButton(bookFrame,
                              width = 150,
                              height=40,
                              text="Ya",
                              font=("Segoe UI Light",20),
                              command= lambda root=root,indicatorArr=indicatorArr,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton,title=title:deleteBuku(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,title))
    yesButton.place(x=200, y =140)

    noButton = ctk.CTkButton(bookFrame,
                              width = 150,
                              height=40,
                              text="Tidak",
                              font=("Segoe UI Light",20),
                              command=lambda root=root,indicatorArr=indicatorArr,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: BC.inginDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton))
    noButton.place(x=450, y =140)
def deleteBuku(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,title):
    # print(title, " dihapus")
    DaftarBukuInginDibaca.hapusBuku(title)
    SaveState.saveBuku()
    BC.inginDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton)

def mulaiBaca(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,title):
    tanggal = datetime.now().strftime("%Y-%m-%d")
    PemindahBuku.PindahBuku(title, tanggal, "")
    SaveState.saveBuku()
    BC.inginDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton)

def tambahBukuPrompt(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton):
    for widget in root.winfo_children():
      widget.destroy()
    tambahFrame = ctk.CTkFrame(root,
                              width=800,
                              height=475,
                              border_color=color,
                              border_width=3)
    tambahFrame.pack(pady = 20)
    promptLabel1 = ctk.CTkLabel(tambahFrame,
                                text="Masukkan buku!",
                                font=("Segoe UI Light", 24))
    promptLabel1.place(x=350, y=10)

    # textinput box
    titleInput = ctk.CTkEntry(tambahFrame,
                                width=550,
                                height=40,
                                font=("Segoe UI Light",20)
                                )
    penulisInput = ctk.CTkEntry(tambahFrame,
                                width=550,
                                height=40,
                                font=("Segoe UI Light",20)
                                )
    penerbitInput = ctk.CTkEntry(tambahFrame,
                                width=550,
                                height=40,
                                font=("Segoe UI Light",20)
                                )
    halamanInput = ctk.CTkEntry(tambahFrame,
                                width=550,
                                height=40,
                                font=("Segoe UI Light",20)
                                )            
    titleInput.place(x=200, y=75)
    penulisInput.place(x=200, y=150)
    penerbitInput.place(x=200, y=225)
    halamanInput.place(x=200, y=300)

    #textInput labels
    titleLabel = ctk.CTkLabel(tambahFrame, 
                                  text="Judul", 
                                  font=("Segoe UI Light", 20))
    titleLabel.place(x=30,y=80)    

    penulisLabel = ctk.CTkLabel(tambahFrame, 
                                  text="Penulis", 
                                  font=("Segoe UI Light", 20))
    penulisLabel.place(x=30,y=155)

    penerbitLabel = ctk.CTkLabel(tambahFrame, 
                                  text="Penerbit", 
                                  font=("Segoe UI Light", 20))
    penerbitLabel.place(x=30,y=230)

    halamanLabel = ctk.CTkLabel(tambahFrame, 
                                  text="Jumlah halaman", 
                                  font=("Segoe UI Light", 20))
    halamanLabel.place(x=30,y=305)


    #command untuk membuat buku
    yesButton = ctk.CTkButton(tambahFrame,
                              width = 150,
                              height=40,
                              text="Buat buku",
                              font=("Segoe UI Light",20),
                              command=lambda root=root,indicatorArr=indicatorArr,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton, titleInput=titleInput, penulisInput=penulisInput, penerbitInput=penerbitInput, halamanInput=halamanInput: tambahBuku(root, indicatorArr, indicator, color, defaultColor, buttonArr, currentButton, titleInput, penulisInput, penerbitInput, halamanInput))
    yesButton.place(x=600, y=400)

    noButton = ctk.CTkButton(tambahFrame,
                              width = 150,
                              height=40,
                              text="Kembali",
                              font=("Segoe UI Light",20),
                              command=lambda root=root,indicatorArr=indicatorArr,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: BC.inginDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton))
    noButton.place(x=50, y=400)  

def tambahBuku(root, indicatorArr, indicator, color, defaultColor, buttonArr, currentButton, titleInput, penulisInput, penerbitInput, halamanInput):
      title=titleInput.get()
      penulis=penulisInput.get()
      penerbit=penerbitInput.get()
      try:
        halaman=int(halamanInput.get())
      except:
        messagebox.showerror("Kesalahan input", "Jumlah halaman hanya boleh diisi oleh bilangan bulat positif!")
        return

      if (len(title)>75):
        messagebox.showerror("Batas input maksimum", "Judul buku tidak boleh lebih dari 75 karakter!")
        return
      if (len(penulis)>75):
        messagebox.showerror("Batas input maksimum", "Nama penulis tidak boleh lebih dari 75 karakter!")
        return
      if (len(penerbit)>75):
        messagebox.showerror("Batas input maksimum", "Nama penerbit tidak boleh lebih dari 75 karakter!")
        return
      if (halaman <= 0):
        messagebox.showerror("Input tidak valid", "Nilai halaman harus bilangan bulat positif!")
        return
      if(title == "" or penulis == "" or penerbit == "" or halaman is None):
        messagebox.showerror("Input kosong", "Semua bagian harus terisi!")
        return
      
      DaftarBukuInginDibaca.tambahBuku(BukuInginDibaca(title, penulis, penerbit, halaman))
      SaveState.saveBuku()
      BC.inginDibacaPage(root, indicatorArr, indicator, color, defaultColor, buttonArr, currentButton)

