from Buku import *
from tkinter import *
from tkinter import messagebox  
import customtkinter as ctk
import ButtonController as BC
import CustomWidget as CW

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
                                 height=430,
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
        bookLastDateLabel =ctk.CTkLabel(bookFrame, 
                                      text="Tanggal terakhir membaca: "+str(temp.tanggalTerakhirBaca), 
                                      font=("Segoe UI Light", 20))
        bookLastDateLabel.place(x=20,y=210)
        bookDayLabel = ctk.CTkLabel(bookFrame, 
                                      text="Durasi membaca: "+str(temp.hariPembacaan)+" hari", 
                                      font=("Segoe UI Light", 20))
        bookDayLabel.place(x=20,y=240)
        bookNoteLabel = ctk.CTkLabel(bookFrame, 
                                      text="Catatan: ", 
                                      font=("Segoe UI Light", 20))
        bookNoteLabel.place(x=20,y=270)
        bookNoteTextBox = ctk.CTkTextbox(bookFrame,
                                         width=670,
                                         height=80,
                                         font=("Segoe UI Light", 20))
        bookNoteTextBox.place(x=100,y=270)
        bookNoteTextBox.insert(1.0,temp.catatan)
        bookNoteTextBox.configure(state="disabled")
        #tombol untuk mengedit data buku
        editBukuButton = ctk.CTkButton(bookFrame,
                                        width = 150,
                                        height=40,
                                        text="Edit Buku",
                                        font=("Segoe UI Light",20),
                                        command=lambda root=root,indicatorArr=indicatorArr,bookFrame=bookFrame,title=temp.judul,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: editBukuPrompt(False,root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title))
        

        #tombol untuk menghapus buku yang sedang dibaca
        hapusBukuButton = ctk.CTkButton(bookFrame,
                                        width = 150,
                                        height=40,
                                        text="Hapus Buku",
                                        font=("Segoe UI Light",20),
                                        fg_color="#B32B3D",
                                        hover_color="#821F2C",
                                        command=lambda root=root,indicatorArr=indicatorArr,bookFrame=bookFrame,title=temp.judul,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: hapusBukuSedangDibacaPrompt(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title))
        if(temp.halamanTerakhir == temp.totalHalaman): #jika sudah di halaman terakhir, tampilkan tombol selesai baca
            selesaibacaBukuButton = ctk.CTkButton(bookFrame,
                                        width = 150,
                                        height=40,
                                        text="Selesai Baca",
                                        font=("Segoe UI Light",20),
                                        command=lambda root=root,indicatorArr=indicatorArr,bookFrame=bookFrame,title=temp.judul,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: selesaiBacaBukuPrompt(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title))
            selesaibacaBukuButton.place(x=620,y=370)
            editBukuButton.place(x=450,y=370)
            hapusBukuButton.place(x=280, y =370)
        else:
            updateKemajuanBukuButton = ctk.CTkButton(bookFrame,
                                        width = 150,
                                        height=40,
                                        text="Ubah Kemajuan",
                                        font=("Segoe UI Light",20),
                                        command=lambda root=root,indicatorArr=indicatorArr,bookFrame=bookFrame,title=temp.judul,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: editBukuPrompt(True,root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title))
            updateKemajuanBukuButton.place(x=620,y=370)
            editBukuButton.place(x=450,y=370)
            hapusBukuButton.place(x=280,y=370)


def hapusBukuSedangDibacaPrompt(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title):
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


def editBukuPrompt(isEditingProgress,root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title):
    teks = ""
    xPos = 0
    yPos = 10
    for widget in bookFrame.winfo_children():
      widget.destroy()
    if(isEditingProgress):
        teks = "Apakah Anda ingin memperbarui kemajuan membaca buku ini?"
        xPos = 130
    else:
        teks = "Apakah Anda ingin mengedit buku ini?"
        xPos = 230
    promptLabel1 = ctk.CTkLabel(bookFrame,
                                text=teks,
                                font=("Segoe UI Light", 20))
    promptLabel1.place(x=xPos,y=yPos)
    if(isEditingProgress):
        yesButton = ctk.CTkButton(bookFrame,
                                  width = 150,
                                  height=40,
                                  text="Ya",
                                  font=("Segoe UI Light",20),
                                  command= lambda root=root,indicatorArr=indicatorArr,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton,title=title:updateKemajuanForm(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton, bookFrame, title))
        yesButton.place(x=200, y =340)
    else:
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

def updateKemajuanForm(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton, bookFrame, title):
    for widget in bookFrame.winfo_children():
      widget.destroy()
    
    bookIndex = DaftarBukuSedangDibaca.getIndex(title)
    temp = DaftarBukuSedangDibaca.listBukuSedangDibaca[bookIndex]
    bookLastPageLabel = ctk.CTkLabel(bookFrame, 
                                    text="Halaman terakhir yang dibaca: ", 
                                    font=("Segoe UI Light", 20))
    bookLastPageLabel.place(x=100, y=170)

    bookLastPageEntry = CW.IntegerSpinbox(bookFrame, width=300, step_size=1)
    bookLastPageEntry.place(x=380, y=170)
    bookLastPageEntry.set(temp.halamanTerakhir)

    cancelButton = ctk.CTkButton(bookFrame,
                                width = 150,
                                height=40,
                                text="Batal",
                                fg_color="#B32B3D",
                                hover_color="#821F2C",
                                font=("Segoe UI Light",18),
                                command= lambda root=root,indicatorArr=indicatorArr,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: BC.sedangDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton))
    cancelButton.place(x=200, y =340)

    #hitung selisih hari
    dayStart =datetime.strptime(temp.tanggalMulaiBaca, "%Y-%m-%d")
    dayNow = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")
    dayDifference = int((dayNow-dayStart).days)
    # Create button to save edited book
    saveButton = ctk.CTkButton(bookFrame,
                                width = 150,
                                height=40,
                                text="Simpan",
                                font=("Segoe UI Light",18),
                                command= lambda root=root,indicatorArr=indicatorArr,indicator=indicator,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: saveEditBuku(root,indicatorArr,indicator,color,defaultColor,buttonArr,currentButton, temp.judul, temp.penulis, temp.penerbit, temp.totalHalaman, bookLastPageEntry.get(), temp.tanggalMulaiBaca, datetime.now().strftime("%Y-%m-%d"), dayDifference, temp.catatan, temp))
    saveButton.place(x=450, y =340)
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

    bookTotalPageEntry = CW.IntegerSpinbox(bookFrame, width=150, step_size=1)
    bookTotalPageEntry.place(x=300, y=130)
    bookTotalPageEntry.set(temp.totalHalaman)

    bookFirstDateLabel = ctk.CTkLabel(bookFrame, 
                                    text="Tanggal mulai membaca: ", 
                                    font=("Segoe UI Light", 16))
    bookFirstDateLabel.place(x=20, y=170)

    # Disable entry for bookFirstDateEntry
    bookFirstDateEntry = ctk.CTkEntry(bookFrame,
                                    width=480,
                                    font=("Segoe UI Light", 16))
    bookFirstDateEntry.place(x=300, y=170)
    bookFirstDateEntry.insert(0, temp.tanggalMulaiBaca)
    bookFirstDateEntry.configure(state='disabled')

    bookLastDateLabel = ctk.CTkLabel(bookFrame, 
                                    text="Tanggal terakhir membaca: ", 
                                    font=("Segoe UI Light", 16))
    bookLastDateLabel.place(x=20, y=210)

    # Disable entry for bookFirstDateEntry
    bookLastDateEntry = ctk.CTkEntry(bookFrame,
                                    width=480,
                                    font=("Segoe UI Light", 16))
    bookLastDateEntry.place(x=300, y=210)
    bookLastDateEntry.insert(0, datetime.now().strftime("%Y-%m-%d"))
    bookLastDateEntry.configure(state='disabled')

    bookNoteLabel = ctk.CTkLabel(bookFrame, 
                                text="Catatan: ", 
                                font=("Segoe UI Light", 16))
    bookNoteLabel.place(x=20, y=250)
    bookNoteEntry = ctk.CTkTextbox(bookFrame,
                                width=480,
                                height=60,
                                font=("Segoe UI Light", 16))
    bookNoteEntry.place(x=300, y=250)
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
    cancelButton.place(x=200, y =340)

    #hitung selisih hari
    dayStart =datetime.strptime(bookFirstDateEntry.get(), "%Y-%m-%d")
    dayNow = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")
    dayDifference = int((dayNow-dayStart).days)
    # Create button to save edited book
    saveButton = ctk.CTkButton(bookFrame,
                                width = 150,
                                height=40,
                                text="Simpan",
                                font=("Segoe UI Light",18),
                                command= lambda root=root,indicatorArr=indicatorArr,indicator=indicator,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: saveEditBuku(root,indicatorArr,indicator,color,defaultColor,buttonArr,currentButton, bookTitleEntry.get(), bookWriterEntry.get(), bookPublisherEntry.get(), bookTotalPageEntry.get(), temp.halamanTerakhir, bookFirstDateEntry.get(), datetime.now().strftime("%Y-%m-%d"), dayDifference, bookNoteEntry.get("1.0",END), temp))
    saveButton.place(x=450, y =340)


def saveEditBuku(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton, judulBaru, penulisBaru, penerbitBaru, totalHalamanBaru, halamanTerakhirBaru, tanggalMulaiBacaBaru, tanggalTerakhirBacaBaru, hariPembacaanBaru, catatanBaru, instansBuku):

    # Input Handling
    if(judulBaru == "" or penulisBaru == "" or penerbitBaru == "" or hariPembacaanBaru is None):
        messagebox.showerror("Input kosong", "Hanya catatan yang boleh kosong!")
        return
    if(totalHalamanBaru is None or halamanTerakhirBaru is None):
        messagebox.showerror("Input tidak valid", "Nilai halaman tidak valid!")
        return
    # Halaman terakhir yang dibaca tidak boleh lebih besar dari jumlah halaman dan tidak boleh kurang dari 0
    if(int(halamanTerakhirBaru) < 0 or int(totalHalamanBaru) <= 0):
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
    
    if (halamanTerakhirBaru > totalHalamanBaru):
        halamanTerakhirBaru = totalHalamanBaru
        messagebox.showinfo("Halaman maksimum", "Input halaman terakhir yang dibaca melebihi total halaman buku.\nHalaman terakhir yang dibaca telah disesuaikan dengan total halaman buku")

    instansBuku.editBuku(judulBaru, penulisBaru, penerbitBaru, totalHalamanBaru, halamanTerakhirBaru, tanggalMulaiBacaBaru, tanggalTerakhirBacaBaru, hariPembacaanBaru, catatanBaru)
    SaveState.saveBuku()
    BC.sedangDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton)

def deleteBuku(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,title):
    DaftarBukuSedangDibaca.hapusBuku(title)
    SaveState.saveBuku()
    BC.sedangDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton)

def selesaiBacaBukuPrompt(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,bookFrame,title):
    for widget in bookFrame.winfo_children():
      widget.destroy()
    promptLabel1 = ctk.CTkLabel(bookFrame,
                                text="Apakah Anda ingin menandai buku ini sudah selesai dibaca?",
                                font=("Segoe UI Light", 20))
    promptLabel1.place(x=150,y=10)

    yesButton = ctk.CTkButton(bookFrame,
                              width = 150,
                              height=40,
                              text="Ya",
                              font=("Segoe UI Light",20),
                              command=lambda root=root,indicatorArr=indicatorArr,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: selesaiBaca(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,title))
    yesButton.place(x=200, y =340)

    noButton = ctk.CTkButton(bookFrame,
                              width = 150,
                              height=40,
                              text="Tidak",
                              font=("Segoe UI Light",20),
                              command=lambda root=root,indicatorArr=indicatorArr,color=color,defaultColor=defaultColor,buttonArr=buttonArr,currentButton=currentButton: BC.sedangDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton))
    noButton.place(x=450, y =340)

def selesaiBaca(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton,title):
    CekSelesai.CekSelesai(title)
    SaveState.saveBuku()
    BC.sedangDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton)