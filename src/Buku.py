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
    def __init__(self, judul: str, penulis: str, penerbit: str, totalHalaman: int, halamanTerakhir: int, tanggalMulaiBaca: str, tanggalTerakhirBaca: str, hariPembacaan:int, catatan:str) -> None:
        super().__init__(judul, penulis, penerbit, totalHalaman)
        self.halamanTerakhir = halamanTerakhir
        self.tanggalMulaiBaca = tanggalMulaiBaca
        self.tanggalTerakhirBaca = tanggalTerakhirBaca
        self.hariPembacaan = hariPembacaan
        self.catatan = catatan
    
    def editBuku(self, judul: str, penulis: str, penerbit: str, totalHalaman: int, halamanTerakhir: int, tanggalMulaiBaca: str, tanggalTerakhirBaca: str, hariPembacaan:int, catatan:str) -> None:
        super().editBuku(judul, penulis, penerbit, totalHalaman)
        self.halamanTerakhir = halamanTerakhir
        self.tanggalMulaiBaca = tanggalMulaiBaca
        self.tanggalTerakhirBaca = tanggalTerakhirBaca
        self.hariPembacaan = hariPembacaan
        self.catatan = catatan
    
class BukuSudahDibaca(Buku):
    def __init__(self, judul: str, penulis: str, penerbit: str, totalHalaman: int, hariSelesai: int, catatan: str, tanggalTerakhirBaca : str) -> None:
        super().__init__(judul, penulis, penerbit, totalHalaman)
        self.hariSelesai = hariSelesai
        self.catatan = catatan
        self.tanggalTerakhirBaca = tanggalTerakhirBaca
    
    def editBuku(self, judul: str, penulis: str, penerbit: str, totalHalaman: int, hariSelesai: int, catatan: str, tanggalTerakhirBaca : str) -> None:
        super().editBuku(judul, penulis, penerbit, totalHalaman)
        self.hariSelesai = hariSelesai
        self.catatan = catatan
        self.tanggalTerakhirBaca = tanggalTerakhirBaca

class DaftarBukuInginDibaca:
    listBukuInginDibaca : list[BukuInginDibaca] = []

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
            raise Exception(f"Tidak ditemukan buku dengan judul {judulBuku}")

    @staticmethod
    def getIndex(judulBuku : str) -> int:
        i = 0
        while (i < len(DaftarBukuInginDibaca.listBukuInginDibaca)):
            if DaftarBukuInginDibaca.listBukuInginDibaca[i].judul == judulBuku:
                return i
            else :
                i+=1
        return -1

    
class DaftarBukuSedangDibaca:
    listBukuSedangDibaca : list[BukuSedangDibaca] = []

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
            raise Exception(f"tidak ditemukan buku dengan judul {judulBuku}")

    @staticmethod
    def getIndex(judulBuku : str) -> int:
        i = 0
        while (i < len(DaftarBukuSedangDibaca.listBukuSedangDibaca)):
            if DaftarBukuSedangDibaca.listBukuSedangDibaca[i].judul == judulBuku:
                return i
            else :
                i+=1
        return -1
        

class DaftarBukuSudahDibaca:
    listBukuSudahDibaca : list[BukuSudahDibaca] = []

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
            raise Exception(f"tidak ditemukan buku dengan judul {judulBuku}")

    @staticmethod
    def getIndex(judulBuku : str) -> int:
        i = 0
        while (i < len(DaftarBukuSudahDibaca.listBukuSudahDibaca)):
            if DaftarBukuSudahDibaca.listBukuSudahDibaca[i].judul == judulBuku:
                return i
            else :
                i+=1
        return -1

class FormIsiDataBuku:
    @staticmethod
    def UploadBuku() -> None:
        Judul = input("Masukkan judul buku : ")
        Penulis = input("Masukkan nama penulis : ")
        Penerbit = input("Masukkan penerbit : ")
        totalHalaman = int(input("Masukkan total halaman : "))
        bukuAdd = BukuInginDibaca(judul=Judul, penulis=Penulis, penerbit=Penerbit, totalHalaman=totalHalaman)
        DaftarBukuInginDibaca.tambahBuku(bukuAdd)


class FormKemajuanBuku:
    @staticmethod
    def UpdateBuku(judul:str, tambahHalaman:int) -> None:
        i = 0
        found = False
        while (i < len(DaftarBukuSedangDibaca.listBukuSedangDibaca) and not found):
            if (DaftarBukuSedangDibaca.listBukuSedangDibaca[i].judul == judul):
                found = True
            else:
                i+=1
        if found:
            DaftarBukuSedangDibaca.listBukuSedangDibaca[i].hariPembacaan += 1
            DaftarBukuSedangDibaca.listBukuSedangDibaca[i].tanggalTerakhirBaca = datetime.now().strftime("%Y-%m-%d")
            if (DaftarBukuSedangDibaca.listBukuSedangDibaca[i].halamanTerakhir+tambahHalaman > DaftarBukuSedangDibaca.listBukuSedangDibaca[i].totalHalaman):
                DaftarBukuSedangDibaca.listBukuSedangDibaca[i].halamanTerakhir = DaftarBukuSedangDibaca.listBukuSedangDibaca[i].totalHalaman
            else:
                DaftarBukuSedangDibaca.listBukuSedangDibaca[i].halamanTerakhir += tambahHalaman
            CekSelesai.CekSelesai(judul)
        else:
            raise Exception(f"tidak ditemukan buku yang sedang dibaca dengan judul {judul}")

class PemindahBuku:
    @staticmethod
    def PindahBuku(judul:str, tanggal:str, catatan:str) -> None:
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
        if (not foundInginDibaca):
            i = 0
            while(not foundInginDibaca and not foundSudahDibaca and i < len(DaftarBukuSudahDibaca.listBukuSudahDibaca)):
                if (DaftarBukuSudahDibaca.listBukuSudahDibaca[i].judul == judul):
                    foundSudahDibaca = True
                else:
                    i+=1
        # jika buku di daftaringindibaca
        if (foundInginDibaca):
            temp = DaftarBukuInginDibaca.listBukuInginDibaca[i]
            DaftarBukuInginDibaca.hapusBuku(temp.judul)
            DaftarBukuSedangDibaca.tambahBuku(BukuSedangDibaca(temp.judul, temp.penulis, temp.penerbit, temp.totalHalaman, 0, tanggal, tanggal, 0, catatan))
        elif (foundSudahDibaca):
            temp = DaftarBukuSudahDibaca.listBukuSudahDibaca[i]
            DaftarBukuSudahDibaca.hapusBuku(temp.judul)
            DaftarBukuSedangDibaca.tambahBuku(BukuSedangDibaca(temp.judul, temp.penulis, temp.penerbit, temp.totalHalaman, 0, tanggal, tanggal, 0, catatan))
        else:
            raise Exception(f"tidak ditemukan buku ingin dibaca atau sudah dibaca dengan judul {judul}")

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
                DaftarBukuSedangDibaca.hapusBuku(temp.judul)
                DaftarBukuSudahDibaca.tambahBuku(BukuSudahDibaca(temp.judul, temp.penulis, temp.penerbit, temp.totalHalaman, temp.hariPembacaan, temp.catatan, temp.tanggalTerakhirBaca))
        else:
            raise Exception(f"tidak ditemukan buku yang sedang dibaca dengan judul {judul}")

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
                print(f"{i}. judul = {temp.judul}, penulis = {temp.penulis}, penerbit = {temp.penerbit}, totalHalaman = {temp.totalHalaman}, halaman terakhir = {temp.halamanTerakhir}, tanggal mulai baca = {temp.tanggalMulaiBaca}, tanggal terakhir baca = {temp.tanggalTerakhirBaca}, hari baca ke-{temp.hariPembacaan}, catatan = {temp.catatan}")
                i+=1
            print()
        if (len(DaftarBukuSudahDibaca.listBukuSudahDibaca) != 0):
            i = 1
            print("===Buku Sudah Dibaca===")
            for temp in DaftarBukuSudahDibaca.listBukuSudahDibaca:
                print(f"{i}. judul = {temp.judul}, penulis = {temp.penulis}, penerbit = {temp.penerbit}, totalHalaman = {temp.totalHalaman}, hari selesai = {temp.hariSelesai}, catatan = {temp.catatan}, tanggal terakhir baca = {temp.tanggalTerakhirBaca}")
                i+=1
            print()

class LoadState:
    @staticmethod
    def loadBuku(databaseFolder : str = "../src/db") -> None:
        DaftarBukuInginDibaca.listBukuInginDibaca = pickle.load(open(f"{databaseFolder}/BukuInginDibaca.dat", "rb"))
        DaftarBukuSedangDibaca.listBukuSedangDibaca = pickle.load(open(f"{databaseFolder}/BukuSedangDibaca.dat", "rb"))
        DaftarBukuSudahDibaca.listBukuSudahDibaca = pickle.load(open(f"{databaseFolder}/BukuSudahDibaca.dat", "rb"))

class SaveState:
    @staticmethod
    def saveBuku() -> None:
        pickle.dump(DaftarBukuInginDibaca.listBukuInginDibaca, open("../src/db/BukuInginDibaca.dat", "wb"))
        pickle.dump(DaftarBukuSedangDibaca.listBukuSedangDibaca, open("../src/db/BukuSedangDibaca.dat", "wb"))
        pickle.dump(DaftarBukuSudahDibaca.listBukuSudahDibaca, open("../src/db/BukuSudahDibaca.dat", "wb"))

