import math

# =========================
# 🔷 CLASS INDUK
# =========================
class BangunDatar:
    def luas(self):
        pass

    def keliling(self):
        pass


# =========================
# 🔷 PERSEGI
# =========================
class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

    def keliling(self):
        return 4 * self.sisi


# =========================
# 🔷 PERSEGI PANJANG
# =========================
class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)


# =========================
# 🔷 LINGKARAN
# =========================
class Lingkaran(BangunDatar):
    def __init__(self, jari2):
        self.jari2 = jari2

    def luas(self):
        return math.pi * self.jari2 ** 2

    def keliling(self):
        return 2 * math.pi * self.jari2
    
    print("Pilih bangun datar:")
print("1. Persegi")
print("2. Persegi Panjang")
print("3. Lingkaran")

pilihan = input("Masukkan pilihan (1/2/3): ")

if pilihan == "1":
    sisi = float(input("Masukkan sisi: "))
    bangun = Persegi(sisi)

elif pilihan == "2":
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    bangun = PersegiPanjang(panjang, lebar)

elif pilihan == "3":
    jari2 = float(input("Masukkan jari-jari: "))
    bangun = Lingkaran(jari2)

else:
    print("Pilihan tidak valid!")
    exit()

print("Luas:", bangun.luas())
print("Keliling:", bangun.keliling())