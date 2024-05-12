import SplashScreen as ss
import MainMenuScreen as mms
import customtkinter as ctk
import BukuInginDibacaPage as BID
#tombol untuk pindah ke menu utama
def switchToMenu(root):
  mms.create(root) 
#tombol untuk pindah ke splash screen
def switchToSplash(root):
  ss.create(root)
#tombol untuk menampilkan semua buku yang ingin dibaca
def inginDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton):
   for widget in root.winfo_children():
      widget.destroy()
   indicate(indicatorArr,indicator, color,defaultColor,buttonArr,currentButton)
   lb = ctk.CTkLabel(root, text="Daftar buku yang ingin dibaca", font=("Segoe UI Light",24))
   lb.pack(pady=15)
   BID.createInginDibacaPage(root,color)
#tombol untuk menampilkan semua buku yang sedang dibaca
def sedangDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton):
   for widget in root.winfo_children():
      widget.destroy()
   indicate(indicatorArr,indicator, color,defaultColor,buttonArr,currentButton)
   lb = ctk.CTkLabel(root, text="Daftar buku yang sedang dibaca", font=("Segoe UI Light",24))
   lb.pack(pady=15)
   for x in range(20):
        ctk.CTkButton(root, text="Sedang dibaca dummy button").pack(pady =20)
#tombol untuk menampilkan semua buku yang sudah dibaca
def sudahDibacaPage(root,indicatorArr,indicator, color,defaultColor,buttonArr,currentButton):
   for widget in root.winfo_children():
      widget.destroy()
   indicate(indicatorArr,indicator, color,defaultColor,buttonArr,currentButton)
   lb = ctk.CTkLabel(root, text="Daftar buku yang sudah dibaca", font=("Segoe UI Light",24))
   lb.pack(pady=15)
   for x in range(20):
        ctk.CTkButton(root, text="Sudah dibaca dummy button").pack(pady =20)        
#perintah untuk mengubah indikator tombol
def indicate(indicatorArr,indicator, color,defaultColor,buttonArr,currentButton):
   hideAllIndicators(indicatorArr,defaultColor,buttonArr)
   indicator.configure(fg_color=color)
   currentButton.configure(text_color=color)
#perintah untuk mematikan semua indikator
def hideAllIndicators(indicatorArr,defaultColor,buttonArr):
   for i in range (len(indicatorArr)):
      indicatorArr[i].configure(fg_color=defaultColor)
      buttonArr[i].configure(text_color="white")