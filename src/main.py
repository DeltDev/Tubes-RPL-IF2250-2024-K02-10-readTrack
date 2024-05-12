from Buku import *

LoadState.loadBuku()

print("Masukkan 'help' ke command untuk mendapat list dari command")
while (True):
    try:
        command = input("\nMasukkan command : ")
        if command == "help":
            print("""
1. "editBuku" = Mengedit informasi buku 
2. "hapusBuku" = Menghapus buku dari database
3. "uploadBuku" = Menambah buku baru ke daftar ingin dibaca
4. "updateBuku" = Memperbarui progress membaca buku yang sedang dibaca
5. "pindahBuku" = Memindah buku dari daftar buku ingin/sudah dibaca ke daftar buku sedang dibaca
6. "cetakBuku" = Mencetak seluruh buku di database
7. "saveBuku" = Menyimpan progress sekarang ke database
8. "stop" = menghentikan program
""")
            
        elif command == "editBuku":
            judul = input("Masukkan judul buku yang ingin diedit: ")
            if (DaftarBukuInginDibaca.getIndex(judul) != -1):
                idx = DaftarBukuInginDibaca.getIndex(judul)
                print("Buku ada di daftar buku yang ingin dibaca, \ninput 'SAMA' untuk string dan -1 untuk integer jika tidak ingin mengganti attribute")
                tjudul = input("masukkan judul : ")
                if (tjudul == "SAMA"):
                    tjudul = DaftarBukuInginDibaca.listBukuInginDibaca[idx].judul
                tpenulis = input("masukkan penulis : ")
                if (tpenulis == "SAMA"):
                    tpenulis = DaftarBukuInginDibaca.listBukuInginDibaca[idx].penulis
                tpenerbit = input("masukkan penerbit : ")
                if (tpenerbit == "SAMA"):
                    tpenerbit = DaftarBukuInginDibaca.listBukuInginDibaca[idx].penerbit
                thalaman = int(input("masukkan total halaman: "))
                if (thalaman == -1):
                    thalaman = DaftarBukuInginDibaca.listBukuInginDibaca[idx].totalHalaman
                DaftarBukuInginDibaca.listBukuInginDibaca[idx].editBuku(tjudul, tpenulis, tpenerbit, thalaman)
            elif (DaftarBukuSedangDibaca.getIndex(judul) != -1):
                idx = DaftarBukuSedangDibaca.getIndex(judul)
                print("Buku ada di daftar buku yang sedang dibaca, \ninput 'SAMA' untuk string dan -1 untuk integer jika tidak ingin mengganti attribute")
                tjudul = input("masukkan judul : ")
                if (tjudul == "SAMA"):
                    tjudul = DaftarBukuSedangDibaca.listBukuSedangDibaca[idx].judul
                tpenulis = input("masukkan penulis : ")
                if (tpenulis == "SAMA"):
                    tpenulis = DaftarBukuSedangDibaca.listBukuSedangDibaca[idx].penulis
                tpenerbit = input("masukkan penerbit : ")
                if (tpenerbit == "SAMA"):
                    tpenerbit = DaftarBukuSedangDibaca.listBukuSedangDibaca[idx].penerbit
                thalaman = int(input("masukkan total halaman: "))
                if (thalaman == -1):
                    thalaman = DaftarBukuSedangDibaca.listBukuSedangDibaca[idx].totalHalaman
                thalamanlast = int(input("masukkan halaman terakhir: "))
                if (thalamanlast == -1):
                    thalamanlast = DaftarBukuSedangDibaca.listBukuSedangDibaca[idx].halamanTerakhir
                ttanggal = input("masukkan tanggal pembacaan : ")
                if (ttanggal == "SAMA"):
                    ttanggal = DaftarBukuSedangDibaca.listBukuSedangDibaca[idx].tanggalMulaiBaca
                thari = int(input("masukkan hari pembacaan : "))
                if (thari == -1):
                    thari = DaftarBukuSedangDibaca.listBukuSedangDibaca[idx].hariPembacaan
                tcatatan = input("masukkan catatan : ")
                if (tcatatan == "SAMA"):
                    tcatatan = DaftarBukuSedangDibaca.listBukuSedangDibaca[idx].tanggalMulaiBaca
                DaftarBukuSedangDibaca.listBukuSedangDibaca[idx].editBuku(tjudul, tpenulis, tpenerbit, thalaman, thalamanlast, ttanggal, thari, tcatatan)
            elif (DaftarBukuSudahDibaca.getIndex(judul) != -1):
                idx = DaftarBukuSudahDibaca.getIndex(judul)
                print("Buku ada di daftar buku yang sudah dibaca, \ninput 'SAMA' untuk string dan -1 untuk integer jika tidak ingin mengganti attribute")
                tjudul = input("masukkan judul : ")
                if (tjudul == "SAMA"):
                    tjudul = DaftarBukuSudahDibaca.listBukuSudahDibaca[idx].judul
                tpenulis = input("masukkan penulis : ")
                if (tpenulis == "SAMA"):
                    tpenulis = DaftarBukuSudahDibaca.listBukuSudahDibaca[idx].penulis
                tpenerbit = input("masukkan penerbit : ")
                if (tpenerbit == "SAMA"):
                    tpenerbit = DaftarBukuSudahDibaca.listBukuSudahDibaca[idx].penerbit
                thalaman = int(input("masukkan total halaman: "))
                if (thalaman == -1):
                    thalaman = DaftarBukuSudahDibaca.listBukuSudahDibaca[idx].totalHalaman
                thari = int(input("masukkan hari selesai : "))
                if (thari == -1):
                    thari = DaftarBukuSudahDibaca.listBukuSudahDibaca[idx].hariSelesai
                tcatatan = input("masukkan catatan : ")
                if (tcatatan == "SAMA"):
                    tcatatan = DaftarBukuSudahDibaca.listBukuSudahDibaca[idx].catatan
                DaftarBukuSudahDibaca.listBukuSudahDibaca[idx].editBuku(tjudul, tpenulis, tpenerbit, thalaman, thari, tcatatan)
            else:
                print(f"Tidak ditemukan buku dengan judul {judul} di daftar manapun!")

        elif command == "hapusBuku":
            judul = input("masukkan judul buku yang hendak dihapus dari database : ")
            if (DaftarBukuInginDibaca.getIndex(judul) != -1):
                print(f"Buku dengan judul {judul} ditemukan di daftar buku ingin dibaca")
                DaftarBukuInginDibaca.hapusBuku(judul)
            elif (DaftarBukuSedangDibaca.getIndex(judul) != -1):
                print(f"Buku dengan judul {judul} ditemukan di daftar buku sedang dibaca")
                DaftarBukuSedangDibaca.hapusBuku(judul)
            elif (DaftarBukuSudahDibaca.getIndex(judul) != -1):
                print(f"Buku dengan judul {judul} ditemukan di daftar buku sudah dibaca")
                DaftarBukuSudahDibaca.hapusBuku(judul)
            else:
                print(f"tidak ditemukan buku dengan judul {judul} di mana pun")
        
        elif command == "uploadBuku":
            FormIsiDataBuku.UploadBuku()

        elif command == "updateBuku":
            judul = input("Masukkan judul buku yang ingin diupdate progress membacanya : ")
            if (DaftarBukuSedangDibaca.getIndex(judul) == -1):
                print(f"tidak ditemukan buku dengan judul {judul} di daftar buku sedang dibaca")
            else:
                tambahHalaman = int(input("Masukkan berapa halaman kemajuan : "))
                tambahHari = int(input("Masukkan jumlah hari yang diperlukan : "))
                FormKemajuanBuku.UpdateBuku(judul, tambahHalaman, tambahHari)

        elif command == "pindahBuku":
            judul = input("Masukkan judul buku yang ingin dipindah dari daftar buku yang ingin/sudah dibaca ke daftar sedang dibaca : ")
            tanggal = input("Masukkan tanggal mulai baca : ")
            catatan = input("Masukkan catatan baru : ")
            PemindahBuku.PindahBuku(judul, tanggal, catatan)
        
        elif command == "cetakBuku":
            CetakBuku.CetakBuku()
        
        elif command == "saveBuku":
            SaveState.saveBuku()

        elif command == "stop":
            break

        else:
            print("command tidak valid! silahkan ulangi")

    except Exception as e:
        print("Terjadi error dengan message : ", end="") 
        print(e)
        