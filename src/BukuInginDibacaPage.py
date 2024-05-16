from Buku import *
from tkinter import messagebox
import customtkinter as ctk
import ButtonController as BC
from datetime import datetime
import CustomWidget as CW
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
                                 height=240,
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
        mulaiBacaButton.place(x=620,y=180)
        #tombol untuk mengedit buku yang ingin dibaca
        editBukuButton = ctk.CTkButton(bookFrame,
                                        width = 150,
                                        height=40,
                                        text="Edit Buku",
                                        font=("Segoe UI Light",20),
                                        command=lambda root=root,indicatorArr=indicatorArr,bookFrame=bookFrame,title=temp.judul,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: editBukuPrompt(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title))
        editBukuButton.place(x=450,y=180)
        #tombol untuk menghapus buku yang ingin dibaca
        hapusBukuButton = ctk.CTkButton(bookFrame,
                                        width = 150,
                                        height=40,
                                        text="Hapus Buku",
                                        font=("Segoe UI Light",20),
                                        fg_color="#B32B3D",
                                        hover_color="#821F2C",
                                        command=lambda root=root,indicatorArr=indicatorArr,bookFrame=bookFrame,title=temp.judul,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: hapusBukuInginDibacaPrompt(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title))
        hapusBukuButton.place(x= 280, y =180)

def editBukuPrompt(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title):
  for widget in bookFrame.winfo_children():
      widget.destroy()
  promptLabel1 = ctk.CTkLabel(bookFrame,
                              text="Apakah Anda ingin mengedit buku ini?",
                              font=("Segoe UI Light", 20))
  promptLabel1.place(x=230,y=10)
  yesButton = ctk.CTkButton(bookFrame,
                            width = 150,
                            height=40,
                            text="Ya",
                            font=("Segoe UI Light",20),
                            command= lambda root=root,indicatorArr=indicatorArr,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton,title=title:editBukuForm(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton, bookFrame, title))
  yesButton.place(x=200, y =180)
  noButton = ctk.CTkButton(bookFrame,
                              width = 150,
                              height=40,
                              text="Tidak",
                              font=("Segoe UI Light",20),
                              command=lambda root=root,indicatorArr=indicatorArr,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: BC.inginDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton))
  noButton.place(x=450, y =180)

def editBukuForm(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton, bookFrame, title):
    for widget in bookFrame.winfo_children():
      widget.destroy()
    
    bookIndex = DaftarBukuInginDibaca.getIndex(title)
    temp = DaftarBukuInginDibaca.listBukuInginDibaca[bookIndex]
    
    # Create form edit book here
    bookTitleLabel = ctk.CTkLabel(bookFrame,
                              text="Judul buku: ",
                              font=("Segoe UI Light", 16))
    bookTitleLabel.place(x=20, y=10)

    bookTitleEntry = ctk.CTkEntry(bookFrame,
                                width=480,
                                font=("Segoe UI Light", 16))
    bookTitleEntry.place(x=300, y=10)
    bookTitleEntry.insert(0, temp.judul)

    bookWriterLabel = ctk.CTkLabel(bookFrame, 
                                text="Penulis: ", 
                                font=("Segoe UI Light", 16))
    bookWriterLabel.place(x=20, y=50)

    bookWriterEntry = ctk.CTkEntry(bookFrame,
                                    width=480,
                                    font=("Segoe UI Light", 16))
    bookWriterEntry.place(x=300, y=50)
    bookWriterEntry.insert(0, temp.penulis)

    bookPublisherLabel = ctk.CTkLabel(bookFrame, 
                                    text="Penerbit: ", 
                                    font=("Segoe UI Light", 16))
    bookPublisherLabel.place(x=20, y=90)

    bookPublisherEntry = ctk.CTkEntry(bookFrame,
                                    width=480,
                                    font=("Segoe UI Light", 16))
    bookPublisherEntry.place(x=300, y=90)
    bookPublisherEntry.insert(0, temp.penerbit)

    bookTotalPageLabel = ctk.CTkLabel(bookFrame, 
                                    text="Jumlah halaman: ", 
                                    font=("Segoe UI Light", 16))
    bookTotalPageLabel.place(x=20, y=130)

    bookTotalPageEntry = CW.IntegerSpinbox(bookFrame, width=150, step_size=1)
    bookTotalPageEntry.place(x=300, y=130)
    bookTotalPageEntry.set(temp.totalHalaman)

    cancelButton = ctk.CTkButton(bookFrame,
                                width = 150,
                                height=40,
                                text="Batal",
                                fg_color="#B32B3D",
                                hover_color="#821F2C",
                                font=("Segoe UI Light",18),
                                command= lambda root=root,indicatorArr=indicatorArr,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: BC.inginDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton))
    cancelButton.place(x=200, y =180)
    saveButton = ctk.CTkButton(bookFrame,
                                width = 150,
                                height=40,
                                text="Simpan",
                                font=("Segoe UI Light",18),
                                command= lambda root=root,indicatorArr=indicatorArr,indicator=indicator,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: saveEditBuku(root,indicatorArr,indicator,color,defaultColor,buttonArr,currentButton, bookTitleEntry.get(), bookWriterEntry.get(), bookPublisherEntry.get(), bookTotalPageEntry.get(),temp))
    saveButton.place(x=450, y =180)
def saveEditBuku(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton, judulBaru, penulisBaru, penerbitBaru, totalHalamanBaru,instansBuku):
       # Input Handling
    if(judulBaru == "" or penulisBaru == "" or penerbitBaru == "" or totalHalamanBaru is None):
        messagebox.showerror("Input kosong", "Semua bagian harus terisi!")
        return

    # Halaman terakhir yang dibaca tidak boleh lebih besar dari jumlah halaman dan tidak boleh kurang dari 0
    if(int(totalHalamanBaru) <= 0):
        messagebox.showerror("Input tidak valid", "Nilai halaman tidak valid!")
        return
    
    if(len(judulBaru) > 75):
        messagebox.showerror("Batas input maksimum", "Judul buku tidak boleh lebih dari 75 karakter!")
        return
    
    if(len(penulisBaru) > 75):
        messagebox.showerror("Batas input maksimum", "Nama penulis tidak boleh lebih dari 75 karakter!")
        return
    
    if(len(penerbitBaru) > 75):
        messagebox.showerror("Batas input maksimum", "Nama penerbit tidak boleh lebih dari 75 karakter!")
        return
    instansBuku.editBuku(judulBaru, penulisBaru, penerbitBaru, totalHalamanBaru)
    SaveState.saveBuku()
    BC.inginDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton)
def hapusBukuInginDibacaPrompt(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title):
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
    yesButton.place(x=200, y =180)

    noButton = ctk.CTkButton(bookFrame,
                              width = 150,
                              height=40,
                              text="Tidak",
                              font=("Segoe UI Light",20),
                              command=lambda root=root,indicatorArr=indicatorArr,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: BC.inginDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton))
    noButton.place(x=450, y =180)

def mulaiBacaPrompt(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title):
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
                              command= lambda root=root,indicatorArr=indicatorArr,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton,title=title:mulaiBaca(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,title))
    yesButton.place(x=200, y =180)

    noButton = ctk.CTkButton(bookFrame,
                              width = 150,
                              height=40,
                              text="Tidak",
                              font=("Segoe UI Light",20),
                              command=lambda root=root,indicatorArr=indicatorArr,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: BC.inginDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton))
    noButton.place(x=450, y =180)
def deleteBuku(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,title):
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

