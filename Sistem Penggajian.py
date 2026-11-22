# ==========================================
# PROJECT SISTEM PENGGAJIAN KARYAWAN
# OBJECT ORIENTED PROGRAMMING (OOP)
# FATIH KHAIRUL ADNAN_14012500131_3d-KOM
# ==========================================


# CLASS 1: Karyawan
class Karyawan:

    jumlah_karyawan = 0

    # Constructor
    def __init__(self, nama, jabatan, gaji_pokok):
        self.nama = nama
        self.jabatan = jabatan
        self.__gaji_pokok = gaji_pokok  # Encapsulation

        Karyawan.jumlah_karyawan += 1

    # Property
    @property
    def gaji_pokok(self):
        return self.__gaji_pokok

    # Setter
    @gaji_pokok.setter
    def gaji_pokok(self, nilai):
        if nilai >= 0:
            self.__gaji_pokok = nilai
        else:
            raise ValueError("Gaji tidak boleh negatif!")

    # Method
    def tampilkan_data(self):
        print("Nama Karyawan :", self.nama)
        print("Jabatan       :", self.jabatan)
        print("Gaji Pokok    :", self.format_rupiah(self.gaji_pokok))

    # Class Method
    @classmethod
    def total_karyawan(cls):
        return cls.jumlah_karyawan

    # Static Method
    @staticmethod
    def format_rupiah(nominal):
        return f"Rp {nominal:,.0f}".replace(",", ".")


# CLASS 2: Penggajian
class Penggajian:

    # Constructor
    def __init__(self, karyawan, tunjangan, potongan):
        self.karyawan = karyawan
        self.tunjangan = tunjangan
        self.potongan = potongan

    # Method menghitung gaji
    def hitung_gaji(self):
        return (
            self.karyawan.gaji_pokok
            + self.tunjangan
            - self.potongan
        )

    # Method mencetak slip gaji
    def cetak_slip_gaji(self):
        print("\n====================================")
        print("          SLIP GAJI KARYAWAN")
        print("====================================")

        self.karyawan.tampilkan_data()

        print("Tunjangan     :",
              Karyawan.format_rupiah(self.tunjangan))

        print("Potongan      :",
              Karyawan.format_rupiah(self.potongan))

        print("------------------------------------")
        print("GAJI BERSIH   :",
              Karyawan.format_rupiah(self.hitung_gaji()))

        print("====================================")


# CLASS 3: MainProgram
class MainProgram:

    # Method untuk menjalankan program
    def jalankan(self):

        print("====================================")
        print("       SISTEM PENGGAJIAN KARYAWAN")
        print("====================================")

        try:
            # Input data secara manual
            nama = input("Masukkan Nama Karyawan : ")
            jabatan = input("Masukkan Posisi/Jabatan: ")

            gaji = int(input("Masukkan Gaji Pokok    : Rp "))
            tunjangan = int(input("Masukkan Tunjangan     : Rp "))
            potongan = int(input("Masukkan Potongan      : Rp "))

            # Validasi data
            if not nama.strip() or not jabatan.strip():
                raise ValueError("Nama dan jabatan wajib diisi!")

            if min(gaji, tunjangan, potongan) < 0:
                raise ValueError("Nominal tidak boleh negatif!")

            if potongan > gaji + tunjangan:
                raise ValueError("Potongan melebihi total pendapatan!")

            # Membuat object Karyawan
            karyawan1 = Karyawan(nama, jabatan, gaji)

            # Menggunakan property dan setter
            karyawan1.gaji_pokok = gaji

            # Membuat object Penggajian
            penggajian1 = Penggajian(
                karyawan1,
                tunjangan,
                potongan
            )

            # Menampilkan hasil
            penggajian1.cetak_slip_gaji()

            # Class Method
            print("Jumlah Karyawan:",
                  Karyawan.total_karyawan())

        except ValueError as error:
            print("\nTerjadi Kesalahan:", error)


# ==========================================
# MEMBUAT OBJECT MAIN PROGRAM
# ==========================================

program = MainProgram()
program.jalankan()
