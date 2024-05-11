import pickle
from datetime import datetime

class Buku:
    def __init__(self, judul: str, penulis: str, penerbit: str, totalHalaman:int) -> None:
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit
        self.totalHalaman = totalHalaman

    
    def editBuku(self, judul: str, penulis: str, penerbit: str, totalHalaman:int) -> None:
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit
        self.totalHalaman = totalHalaman

class BukuInginDibaca(Buku):
    def __init__(self, judul: str, penulis: str, penerbit: str, totalHalaman: int) -> None:
        super().__init__(judul, penulis, penerbit, totalHalaman)

class BukuSedangDibaca(Buku):
    def __init__(self, judul: str, penulis: str, penerbit: str, totalHalaman: int, halamanTerakhir: int, tanggalMulaiBaca: datetime, hariPembacaan:int, catatan:str) -> None:
        super().__init__(judul, penulis, penerbit, totalHalaman)
        self.halamanTerakhir = halamanTerakhir
        self.tanggalMulaiBaca = tanggalMulaiBaca
        self.hariPembacaan = hariPembacaan
        self.catatan = catatan
    
    def editBuku(self, judul: str, penulis: str, penerbit: str, totalHalaman: int, halamanTerakhir: int, tanggalMulaiBaca: datetime, hariPembacaan:int, catatan:str) -> None:
        self.halamanTerakhir = halamanTerakhir
        self.tanggalMulaiBaca = tanggalMulaiBaca
        self.hariPembacaan = hariPembacaan
        self.catatan = catatan
        return super().editBuku(judul, penulis, penerbit, totalHalaman)
    
class BukuSudahDibaca(Buku):
    def __init__(self, judul: str, penulis: str, penerbit: str, totalHalaman: int, hariSelesai: int, catatan: str) -> None:
        super().__init__(judul, penulis, penerbit, totalHalaman)
        self.hariSelesai = hariSelesai
        self.catatan = catatan
    
    def editBuku(self, judul: str, penulis: str, penerbit: str, totalHalaman: int, hariSelesai: int, catatan: str) -> None:
        self.hariSelesai = hariSelesai
        self.catatan = catatan
        return super().editBuku(judul, penulis, penerbit, totalHalaman)

class DaftarBukuInginDibaca:
    listBukuInginDibaca : list[BukuInginDibaca] = pickle.load(open("db/BukuInginDibaca.dat", "rb"))

    @staticmethod
    def tambahBuku(bukuDitambah : BukuInginDibaca):
        DaftarBukuInginDibaca.listBukuInginDibaca.append(bukuDitambah)
    
    @staticmethod 
    def hapusBuku(judulBuku : str):
        i = 0
        found = False
        while (i < len(DaftarBukuInginDibaca.listBukuInginDibaca) and not found):
            if (DaftarBukuInginDibaca.listBukuInginDibaca[i].judul == judulBuku):
                found = True
            else:
                i+=1
        if (found):
            temp = DaftarBukuInginDibaca.listBukuInginDibaca[i]
            DaftarBukuInginDibaca.listBukuInginDibaca.remove(temp)
        else:
            print(f"tidak ditemukan buku dengan judul {judulBuku}")
    
class DaftarBukuSedangDibaca:
    listBukuSedangDibaca : list[BukuSedangDibaca] =  pickle.load(open("db/BukuSedangDibaca.dat", "rb"))

    @staticmethod
    def tambahBuku(bukuDitambah : BukuSedangDibaca):
        DaftarBukuSedangDibaca.listBukuSedangDibaca.append(bukuDitambah)
    
    @staticmethod 
    def hapusBuku(judulBuku : str):
        i = 0
        found = False
        while (i < len(DaftarBukuSedangDibaca.listBukuSedangDibaca) and not found):
            if (DaftarBukuSedangDibaca.listBukuSedangDibaca[i].judul == judulBuku):
                found = True
            else:
                i+=1
        if (found):
            temp = DaftarBukuSedangDibaca.listBukuSedangDibaca[i]
            DaftarBukuSedangDibaca.listBukuSedangDibaca.remove(temp)
        else:
            print(f"tidak ditemukan buku dengan judul {judulBuku}")
        

class DaftarBukuSudahDibaca:
    listBukuSudahDibaca : list[BukuSudahDibaca] = pickle.load(open("db/BukuSudahDibaca.dat", "rb"))

    @staticmethod
    def tambahBuku(bukuDitambah : BukuSudahDibaca):
        DaftarBukuSudahDibaca.listBukuSudahDibaca.append(bukuDitambah)
    
    @staticmethod 
    def hapusBuku(judulBuku : str):
        i = 0
        found = False
        while (i < len(DaftarBukuSudahDibaca.listBukuSudahDibaca) and not found):
            if (DaftarBukuSudahDibaca.listBukuSudahDibaca[i].judul == judulBuku):
                found = True
            else:
                i+=1
        if (found):
            temp = DaftarBukuSudahDibaca.listBukuSudahDibaca[i]
            DaftarBukuSudahDibaca.listBukuSudahDibaca.remove(temp)
        else:
            print(f"tidak ditemukan buku dengan judul {judulBuku}")

class FormIsiDataBuku:
    @staticmethod
    def UploadBuku() -> None:
        Judul = input("Masukkan judul buku : ")
        Penulis = input("Masukkan nama penulis : ")
        Penerbit = input("Masukkan penerbit : ")
        totalHalaman = int(input("Masukkan total halaman : "))
        bukuAdd = BukuInginDibaca(judul=Judul, penulis=Penulis, penerbit=Penerbit, totalHalaman=totalHalaman)
        DaftarBukuInginDibaca.listBukuInginDibaca.append(bukuAdd)
        print("Buku berhasil ditambah ke Daftar buku yang ingin dibaca")

class FormKemajuanBuku:
    @staticmethod
    def UpdateBuku(judul:str, tambahHalaman:int, tambahHari:int) -> None:
        i = 0
        found = False
        while (i < len(DaftarBukuSedangDibaca.listBukuSedangDibaca) and not found):
            if (DaftarBukuSedangDibaca.listBukuSedangDibaca[i].judul == judul):
                found = True
            else:
                i+=1
        if found:
            if (DaftarBukuSedangDibaca.listBukuSedangDibaca[i].halamanTerakhir+tambahHalaman >= DaftarBukuSedangDibaca.listBukuSedangDibaca[i].totalHalaman):
                DaftarBukuSedangDibaca.listBukuSedangDibaca[i].halamanTerakhir = DaftarBukuSedangDibaca.listBukuSedangDibaca[i].totalHalaman
            else:
                DaftarBukuSedangDibaca.listBukuSedangDibaca[i].halamanTerakhir += tambahHalaman
                DaftarBukuSedangDibaca.listBukuSedangDibaca[i].hariPembacaan += tambahHari
                print(f"Buku sudah ditambah halaman terakhirnya sebanyak {tambahHalaman}")
            CekSelesai.CekSelesai(judul)
        else:
            print(f"tidak ditemukan buku yang sedang dibaca dengan judul {judul}")

class PemindahBuku:
    @staticmethod
    def PindahBuku(judul:str, tanggal:datetime, catatan:str) -> None:
        i = 0
        foundInginDibaca = False
        foundSudahDibaca = False
        # mencari buku di daftaringindibaca
        while (i < len(DaftarBukuInginDibaca.listBukuInginDibaca) and not foundInginDibaca):
            if (DaftarBukuInginDibaca.listBukuInginDibaca[i].judul == judul):
                foundInginDibaca = True
            else:
                i+=1
        # mencari buku di daftarsudahdibaca
        i = 0
        while(not foundInginDibaca and not foundSudahDibaca and i < len(DaftarBukuSudahDibaca.listBukuSudahDibaca)):
            if (DaftarBukuSudahDibaca.listBukuSudahDibaca[i].judul == judul):
                foundSudahDibaca = True
            else:
                i+=1
        # jika buku di daftaringindibaca
        if (foundInginDibaca):
            temp = DaftarBukuInginDibaca.listBukuInginDibaca[i]
            DaftarBukuInginDibaca.listBukuInginDibaca.remove(temp)
            DaftarBukuSedangDibaca.listBukuSedangDibaca.append(BukuSedangDibaca(temp.judul, temp.penulis, temp.penerbit, temp.totalHalaman, 0, tanggal, 1, catatan))
            print("Buku berhasil dipindah dari daftar ingin dibaca ke daftar sedang dibaca")
        elif (foundSudahDibaca):
            temp = DaftarBukuSudahDibaca.listBukuSudahDibaca[i]
            DaftarBukuSudahDibaca.listBukuSudahDibaca.remove(temp)
            DaftarBukuSedangDibaca.listBukuSedangDibaca.append(BukuSedangDibaca(temp.judul, temp.penulis, temp.penerbit, temp.totalHalaman, 0, tanggal, 1, catatan))
            print("Buku berhasil dipindah dari daftar sudah dibaca ke daftar sedang dibaca")
        else:
            print(f"tidak ditemukan buku ingin dibaca atau sudah dibaca dengan judul {judul}")

class CekSelesai:
    @staticmethod
    def CekSelesai(judul:str) -> None:
        i = 0
        found = False
        while (i < len(DaftarBukuSedangDibaca.listBukuSedangDibaca) and not found):
            if (DaftarBukuSedangDibaca.listBukuSedangDibaca[i].judul == judul):
                found = True
            else:
                i+=1
        if found:
            temp = DaftarBukuSedangDibaca.listBukuSedangDibaca[i]
            if temp.halamanTerakhir == temp.totalHalaman:
                print("Buku sudah selesai dibaca... memindahkan buku ke daftar sudah dibaca")
                DaftarBukuSedangDibaca.listBukuSedangDibaca.remove(temp)
                DaftarBukuSudahDibaca.listBukuSudahDibaca.append(BukuSudahDibaca(temp.judul, temp.penulis, temp.penerbit, temp.totalHalaman, temp.hariPembacaan, temp.catatan))
            else:
                print("Buku belum selesai dibaca")
        else:
            print(f"tidak ditemukan buku yang sedang dibaca dengan judul {judul}")

class CetakBuku:
    @staticmethod
    def CetakBuku() -> None:
        if (len(DaftarBukuInginDibaca.listBukuInginDibaca) != 0):
            i = 1
            print("===Buku Ingin Dibaca===")
            for temp in DaftarBukuInginDibaca.listBukuInginDibaca:
                print(f"{i}. judul = {temp.judul}, penulis = {temp.penulis}, penerbit = {temp.penerbit}, totalHalaman = {temp.totalHalaman}")
                i+=1
            print()
        if (len(DaftarBukuSedangDibaca.listBukuSedangDibaca) != 0):
            i = 1
            print("===Buku Sedang Dibaca===")
            for temp in DaftarBukuSedangDibaca.listBukuSedangDibaca:
                print(f"{i}. judul = {temp.judul}, penulis = {temp.penulis}, penerbit = {temp.penerbit}, totalHalaman = {temp.totalHalaman}, halaman terakhir = {temp.halamanTerakhir}, tanggal mulai baca = {temp.tanggalMulaiBaca}, hari baca ke-{temp.hariPembacaan}, catatan = {temp.catatan}")
                i+=1
            print()
        if (len(DaftarBukuSudahDibaca.listBukuSudahDibaca) != 0):
            i = 1
            print("===Buku Sudah Dibaca===")
            for temp in DaftarBukuSudahDibaca.listBukuSudahDibaca:
                print(f"{i}. judul = {temp.judul}, penulis = {temp.penulis}, penerbit = {temp.penerbit}, totalHalaman = {temp.totalHalaman}, hari selesai = {temp.hariSelesai}, catatan = {temp.catatan}")
                i+=1
            print()


class SaveState:
    def saveBuku() -> None:
        pickle.dump(DaftarBukuInginDibaca.listBukuInginDibaca, open("db/BukuInginDibaca.dat", "wb"))
        pickle.dump(DaftarBukuSedangDibaca.listBukuSedangDibaca, open("db/BukuSedangDibaca.dat", "wb"))
        pickle.dump(DaftarBukuSudahDibaca.listBukuSudahDibaca, open("db/BukuSudahDibaca.dat", "wb"))
        print("State sekarang berhasil disimpan ke database")


CetakBuku.CetakBuku()