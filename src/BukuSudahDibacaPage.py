from Buku import *
from tkinter import *
import customtkinter as ctk
from PIL import Image
import ButtonController as BC
import LogoLoader as LL
from datetime import datetime

LoadState.loadBuku()
def createSudahDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton):
    if(len(DaftarBukuSudahDibaca.listBukuSudahDibaca) == 0):
        messageLabel = ctk.CTkLabel(root, 
                                    text="Anda belum punya buku yang sudah selesai Anda baca!\nYuk selesaikan baca buku yang sedang dibaca!", 
                                    font=("Segoe UI Light",24))
        messageLabel.pack()
        return
    for temp in DaftarBukuSudahDibaca.listBukuSudahDibaca:
        bookFrame = ctk.CTkFrame(root,
                                 width=800,
                                 height=440,
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
        bookFinishDateLabel =ctk.CTkLabel(bookFrame, 
                                      text="Durasi membaca (hari): "+str(temp.hariSelesai), 
                                      font=("Segoe UI Light", 20))
        bookFinishDateLabel.place(x=20,y=150)
        bookLastDateLabel =ctk.CTkLabel(bookFrame, 
                                      text="Tanggal terakhir membaca: "+str(temp.tanggalTerakhirBaca), 
                                      font=("Segoe UI Light", 20))
        bookLastDateLabel.place(x=20,y=180)
        bookNoteLabel = ctk.CTkLabel(bookFrame, 
                                      text="Catatan: ", 
                                      font=("Segoe UI Light", 20))
        bookNoteLabel.place(x=20,y=210)
        bookNoteTextBox = ctk.CTkTextbox(bookFrame,
                                         width=670,
                                         height=130,
                                         font=("Segoe UI Light", 20))
        bookNoteTextBox.place(x=100,y=210)
        bookNoteTextBox.insert(1.0,temp.catatan)
        bookNoteTextBox.configure(state="disabled")
        #tombol untuk memindahkan buku yang sudah dibaca ke list buku yang sedang dibaca
        readAgainButton = ctk.CTkButton(bookFrame,
                                        width = 150,
                                        height=40,
                                        text="Baca Lagi!",
                                        font=("Segoe UI Light",20),
                                        command=lambda root=root,indicatorArr=indicatorArr,bookFrame=bookFrame,title=temp.judul,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: bacaLagiPrompt(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title))
        readAgainButton.place(x=620,y=370)

        #tombol untuk menghapus buku yang ingin dibaca
        hapusBukuButton = ctk.CTkButton(bookFrame,
                                        width = 150,
                                        height=40,
                                        text="Hapus Buku",
                                        font=("Segoe UI Light",20),
                                        fg_color="#B32B3D",
                                        hover_color="#821F2C",
                                        command=lambda root=root,indicatorArr=indicatorArr,bookFrame=bookFrame,title=temp.judul,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: hapusBukuSudahDibacaPrompt(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title))
        hapusBukuButton.place(x= 450, y =370)

def hapusBukuSudahDibacaPrompt(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title):
    # print(title)
    for widget in bookFrame.winfo_children():
      widget.destroy()
    promptLabel1 = ctk.CTkLabel(bookFrame,
                                text="Apakah Anda yakin untuk menghapus buku ini dari daftar buku yang sudah dibaca?",
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
                              command=lambda root=root,indicatorArr=indicatorArr,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: BC.sudahDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton))
    noButton.place(x=450, y =340)
def bacaLagiPrompt(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title):
    print(title)
    for widget in bookFrame.winfo_children():
      widget.destroy()
    promptLabel1 = ctk.CTkLabel(bookFrame,
                                text="Apakah Anda ingin membaca buku ini lagi?",
                                font=("Segoe UI Light", 20))
    promptLabel1.place(x=230,y=10)

    yesButton = ctk.CTkButton(bookFrame,
                              width = 150,
                              height=40,
                              text="Ya",
                              font=("Segoe UI Light",20),
                              command=lambda root=root,indicatorArr=indicatorArr,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: bacaLagi(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,title))
    yesButton.place(x=200, y =340)

    noButton = ctk.CTkButton(bookFrame,
                              width = 150,
                              height=40,
                              text="Tidak",
                              font=("Segoe UI Light",20),
                              command=lambda root=root,indicatorArr=indicatorArr,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: BC.sudahDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton))
    noButton.place(x=450, y =340)
def deleteBuku(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,title):
    # print(title, " dihapus")
    DaftarBukuSudahDibaca.hapusBuku(title)
    SaveState.saveBuku()
    BC.sudahDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton)

def bacaLagi(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,title):
    tanggal = datetime.now().strftime("%Y-%m-%d")
    PemindahBuku.PindahBuku(title, tanggal, "")
    SaveState.saveBuku()
    BC.sudahDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton)