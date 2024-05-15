from tkinter import *
import customtkinter as ctk
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
                          height = 160,
                          corner_radius=0)
  topFrameFG = topFrame.cget("fg_color")
  bottomFrame = ctk.CTkFrame(masterFrame,
                            width=1280,
                            height = 580,
                            corner_radius=0)
  logoFrame = ctk.CTkFrame(topFrame,
                            width = 130,
                            height = 130,
                            fg_color=topFrameFG)
  bookSelectionFrame = ctk.CTkFrame(bottomFrame,
                                    width = 200,
                                    height = 560)
  bookListFrame = ctk.CTkScrollableFrame(bottomFrame,
                               width = 1010,
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
  bookListFrame.pack(side=LEFT)
  readTrackImageLabel = ctk.CTkLabel(logoFrame, text="", image=LL.loadLogo(175,175), width=200, height= 200)
  readTrackImageLabel.pack()
  readTrackImageLabel.pack_propagate(False)
  menuLabel = ctk.CTkLabel(topFrame, text="Daftar Buku", font=("Segoe UI Light", 48))
  menuLabel.pack(pady=20)
  menuLabel2 = ctk.CTkLabel(topFrame, text="readTrack v1.0", font=("Segoe UI Light", 24))
  menuLabel2.pack(side=TOP)
  welcomeLabel = ctk.CTkLabel(bookListFrame, text="Selamat datang di readTrack!\nSilakan akses buku-buku Anda di menu yang ada di sebelah kiri layar ini.", font=("Segoe UI Light", 24))
  welcomeLabel.pack(pady=10)
  backButton = ctk.CTkButton(bookSelectionFrame,
                             text="Kembali",
                             command=lambda: BC.switchToSplash(root),
                             font=("Segoe UI Light", 20),
                             height=50,
                             width=75)
  backButton.pack(side=BOTTOM,pady=15)
  labelCol = backButton.cget("fg_color")
  selFrameCol = bookSelectionFrame.cget("fg_color")
  inginDibacaIndic = ctk.CTkLabel(bookSelectionFrame,text='',height=50,width=75)
  inginDibacaIndic.place(x=15,y=15)
  inginDibacaButton = ctk.CTkButton(bookSelectionFrame,
                             text="Ingin Dibaca",
                             font=("Segoe UI Light", 20),
                             height=50,
                             width=75,
                             fg_color= selFrameCol,
                             command=lambda: BC.inginDibacaPage(bookListFrame,indicateArr,inginDibacaIndic,labelCol,selFrameCol,buttonArr,inginDibacaButton))
  inginDibacaButton.place(x=25,y=15)
  sedangDibacaIndic = ctk.CTkLabel(bookSelectionFrame,text='',height=50,width=75)
  sedangDibacaIndic.place(x=15,y=80)
  sedangDibacaButton = ctk.CTkButton(bookSelectionFrame,
                             text="Sedang Dibaca",
                             font=("Segoe UI Light", 20),
                             height=50,
                             width=75,
                             fg_color=selFrameCol,
                             command=lambda: BC.sedangDibacaPage(bookListFrame,indicateArr,sedangDibacaIndic,labelCol,selFrameCol,buttonArr,sedangDibacaButton))
  sedangDibacaButton.place(x=25,y=80)
  sudahDibacaIndic = ctk.CTkLabel(bookSelectionFrame,text='',height=50,width=75)
  sudahDibacaIndic.place(x=15,y=145)
  sudahDibacaButton = ctk.CTkButton(bookSelectionFrame,
                             text="Sudah Dibaca",
                             font=("Segoe UI Light", 20),
                             height=50,
                             width=75,
                             fg_color=selFrameCol,
                             command=lambda: BC.sudahDibacaPage(bookListFrame,indicateArr,sudahDibacaIndic,labelCol,selFrameCol,buttonArr,sudahDibacaButton))
  indicateArr = [inginDibacaIndic,sedangDibacaIndic,sudahDibacaIndic]
  buttonArr = [inginDibacaButton,sedangDibacaButton,sudahDibacaButton]
  sudahDibacaButton.place(x=25,y=145)
