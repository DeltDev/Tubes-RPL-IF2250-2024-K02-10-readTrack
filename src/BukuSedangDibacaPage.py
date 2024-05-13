from Buku import *
from tkinter import *
import customtkinter as ctk
from PIL import Image
import ButtonController as BC
import LogoLoader as LL

LoadState.loadBuku()
def createSedangDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton):
    if(len(DaftarBukuSedangDibaca.listBukuSedangDibaca) == 0):
        messageLabel = ctk.CTkLabel(root, 
                                    text="Hmm... Anda tidak sedang membaca buku...\nYuk mulai baca buku dari buku-buku yang ingin Anda baca!", 
                                    font=("Segoe UI Light",24))
        messageLabel.pack()
        return
    for temp in DaftarBukuSedangDibaca.listBukuSedangDibaca:
        bookFrame = ctk.CTkFrame(root,
                                 width=800,
                                 height=400,
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
        bookLastPageLabel =ctk.CTkLabel(bookFrame, 
                                      text="Halaman terakhir yang dibaca: "+str(temp.halamanTerakhir), 
                                      font=("Segoe UI Light", 20))
        bookLastPageLabel.place(x=20,y=150)
        bookFirstDateLabel =ctk.CTkLabel(bookFrame, 
                                      text="Tanggal mulai membaca: "+str(temp.tanggalMulaiBaca), 
                                      font=("Segoe UI Light", 20))
        bookFirstDateLabel.place(x=20,y=180)
        bookDayLabel = ctk.CTkLabel(bookFrame, 
                                      text="Hari pembacaan: "+str(temp.hariPembacaan), 
                                      font=("Segoe UI Light", 20))
        bookDayLabel.place(x=20,y=210)
        bookNoteLabel = ctk.CTkLabel(bookFrame, 
                                      text="Catatan: "+str(temp.catatan), 
                                      font=("Segoe UI Light", 20))
        bookNoteLabel.place(x=20,y=240)

        #tombol untuk mengedit data buku
        editBukuButton = ctk.CTkButton(bookFrame,
                                        width = 150,
                                        height=40,
                                        text="Edit Buku",
                                        font=("Segoe UI Light",20),
                                        command=lambda root=root,indicatorArr=indicatorArr,bookFrame=bookFrame,title=temp.judul,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: editBukuPrompt(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title))
        editBukuButton.place(x=620,y=340)

        #tombol untuk menghapus buku yang sedang dibaca
        hapusBukuButton = ctk.CTkButton(bookFrame,
                                        width = 150,
                                        height=40,
                                        text="Hapus Buku",
                                        font=("Segoe UI Light",20),
                                        fg_color="#B32B3D",
                                        hover_color="#821F2C",
                                        command=lambda root=root,indicatorArr=indicatorArr,bookFrame=bookFrame,title=temp.judul,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: hapusBukuSedangDibacaPrompt(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title))
        hapusBukuButton.place(x= 450, y =340)


def hapusBukuSedangDibacaPrompt(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title):
    # print(title)
    for widget in bookFrame.winfo_children():
      widget.destroy()
    promptLabel1 = ctk.CTkLabel(bookFrame,
                                text="Apakah Anda yakin untuk menghapus buku ini dari daftar buku yang sedang dibaca?",
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
    yesButton.place(x=200, y =340)

    noButton = ctk.CTkButton(bookFrame,
                              width = 150,
                              height=40,
                              text="Tidak",
                              font=("Segoe UI Light",20),
                              command=lambda root=root,indicatorArr=indicatorArr,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: BC.sedangDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton))
    noButton.place(x=450, y =340)


def editBukuPrompt(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title):
    print(title)
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
    yesButton.place(x=200, y =340)

    noButton = ctk.CTkButton(bookFrame,
                              width = 150,
                              height=40,
                              text="Tidak",
                              font=("Segoe UI Light",20),
                              command=lambda root=root,indicatorArr=indicatorArr,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: BC.sedangDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton))
    noButton.place(x=450, y =340)


def editBukuForm(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton, bookFrame, title):
    for widget in bookFrame.winfo_children():
      widget.destroy()
    
    bookIndex = DaftarBukuSedangDibaca.getIndex(title)
    temp = DaftarBukuSedangDibaca.listBukuSedangDibaca[bookIndex]
    
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

    bookTotalPageEntry = ctk.CTkEntry(bookFrame,
                                    width=480,
                                    font=("Segoe UI Light", 16))
    bookTotalPageEntry.place(x=300, y=130)
    bookTotalPageEntry.insert(0, temp.totalHalaman)

    bookLastPageLabel = ctk.CTkLabel(bookFrame, 
                                    text="Halaman terakhir yang dibaca: ", 
                                    font=("Segoe UI Light", 16))
    bookLastPageLabel.place(x=20, y=170)

    bookLastPageEntry = ctk.CTkEntry(bookFrame,
                                    width=480,
                                    font=("Segoe UI Light", 16))
    bookLastPageEntry.place(x=300, y=170)
    bookLastPageEntry.insert(0, temp.halamanTerakhir)

    bookFirstDateLabel = ctk.CTkLabel(bookFrame, 
                                    text="Tanggal mulai membaca: ", 
                                    font=("Segoe UI Light", 16))
    bookFirstDateLabel.place(x=20, y=210)

    # Disable entry for bookFirstDateEntry
    bookFirstDateEntry = ctk.CTkEntry(bookFrame,
                                    width=480,
                                    font=("Segoe UI Light", 16))
    bookFirstDateEntry.place(x=300, y=210)
    bookFirstDateEntry.insert(0, temp.tanggalMulaiBaca)
    bookFirstDateEntry.configure(state='disabled')

    bookDayLabel = ctk.CTkLabel(bookFrame, 
                                text="Hari pembacaan: ", 
                                font=("Segoe UI Light", 16))
    bookDayLabel.place(x=20, y=250)

    bookDayEntry = ctk.CTkEntry(bookFrame,
                                width=480,
                                font=("Segoe UI Light", 16))
    bookDayEntry.place(x=300, y=250)
    bookDayEntry.insert(0, temp.hariPembacaan)

    bookNoteLabel = ctk.CTkLabel(bookFrame, 
                                text="Catatan: ", 
                                font=("Segoe UI Light", 16))
    bookNoteLabel.place(x=20, y=290)
    bookNoteEntry = ctk.CTkTextbox(bookFrame,
                                width=480,
                                height=60,
                                font=("Segoe UI Light", 16))
    bookNoteEntry.place(x=300, y=290)
    bookNoteEntry.insert(1.0, temp.catatan)


    # Create button to cance edit book
    cancelButton = ctk.CTkButton(bookFrame,
                                width = 150,
                                height=40,
                                text="Batal",
                                fg_color="#B32B3D",
                                hover_color="#821F2C",
                                font=("Segoe UI Light",18),
                                command= lambda root=root,indicatorArr=indicatorArr,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: BC.sedangDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton))
    cancelButton.place(x=200, y =350)
    # Create button to save edited book
    saveButton = ctk.CTkButton(bookFrame,
                                width = 150,
                                height=40,
                                text="Simpan",
                                font=("Segoe UI Light",18),
                                command= lambda root=root,indicatorArr=indicatorArr,indicator=indicator,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton,bookInstance=temp, judul=bookTitleEntry, penulis=bookWriterEntry, penerbit=bookPublisherEntry, totalHalaman=bookTotalPageEntry, halamanTerakhir=bookLastPageEntry, tanggalMulaiBaca=bookFirstDateEntry, hariPembacaan=bookDayEntry, catatan=bookNoteEntry: saveEditBuku(root,indicatorArr,indicator,color,defaultColor,buttonArr,currentButton,bookInstance, bookTitleEntry.get(), bookWriterEntry.get(), bookPublisherEntry.get(), bookTotalPageEntry.get(), bookLastPageEntry.get(), bookFirstDateEntry.get(), bookDayEntry.get(), bookNoteEntry.get("1.0",END)))
    saveButton.place(x=450, y =350)


def saveEditBuku(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookInstance, judul, penulis, penerbit, totalHalaman, halamanTerakhir, tanggalMulaiBaca, hariPembacaan, catatan):
    bookInstance.editBuku(judul, penulis, penerbit, totalHalaman, halamanTerakhir, tanggalMulaiBaca, hariPembacaan, catatan)
    SaveState.saveBuku()
    BC.sedangDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton)

def deleteBuku(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,title):
    # print(title, " dihapus")
    DaftarBukuSedangDibaca.hapusBuku(title)
    SaveState.saveBuku()
    BC.sedangDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton)