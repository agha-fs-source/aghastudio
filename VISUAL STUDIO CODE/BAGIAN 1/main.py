import mysql.connector

# =========================
# KONEKSI DATABASE
# =========================
def koneksi_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="database_agha"
    )


# =========================
# KONVERSI TEKS KE ANGKA
# =========================
def konversi_angka(cursor, db):
    kamus = {
        "satu"      : 1, 
        "dua"       : 2, 
        "tiga"      : 3, 
        "empat"     : 4, 
        "lima"      : 5,
        "enam"      : 6, 
        "tujuh"     : 7, 
        "delapan"   : 8, 
        "sembilan"  : 9, 
        "sepuluh"   : 10
    }

    cursor.execute("SELECT id, angka FROM angka")
    records = cursor.fetchall()

    for rec in records:
        idx, teks = rec

        if teks in kamus:
            nilai = kamus[teks]

            cursor.execute(
                "UPDATE angka SET angka=%s WHERE id=%s",
                (nilai, idx)
            )

    db.commit()


# =========================
# TAMPILKAN DATA + JENIS
# =========================
def tampilkan_data(cursor):
    cursor.execute("SELECT * FROM angka ORDER BY angka ASC")
    hasil = cursor.fetchall()

    print("+----+----------+---------+")
    print("| id | angka    | jenis   |")
    print("+----+----------+---------+")

    for item in hasil:
        nomor = int(item[1])

        jenis = "Genap" if nomor % 2 == 0 else "Ganjil"

        print(f"| {item[0]:<2} | {nomor:<8} | {jenis:<7} |")

    print("+----+----------+---------+")


# =========================
# HAPUS DATA
# =========================
def hapus_data(cursor, db):
    pilihan = input("\nMau hapus (ganjil/genap)? ").strip().lower()

    if pilihan == "ganjil":
        query = "DELETE FROM angka WHERE MOD(angka,2)=1"
    elif pilihan == "genap":
        query = "DELETE FROM angka WHERE MOD(angka,2)=0"
    else:
        print("Input tidak dikenali!")
        return

    cursor.execute(query)
    db.commit()
    print("Data berhasil dihapus!")


# =========================
# TAMPIL AKHIR
# =========================
def tampil_akhir(cursor):
    cursor.execute("SELECT * FROM angka ORDER BY angka ASC")
    data = cursor.fetchall()

    print("\n+----+----------+")
    print("| id | angka    |")
    print("+----+----------+")

    for d in data:
        print(f"| {d[0]:<2} | {d[1]:<8} |")

    print("+----+----------+")


# =========================
# MAIN PROGRAM
# =========================
def main():
    try:
        db = koneksi_db()
        cur = db.cursor()

        konversi_angka(cur, db)
        tampilkan_data(cur)
        hapus_data(cur, db)
        tampil_akhir(cur)

        cur.close()
        db.close()

    except mysql.connector.Error as err:
        print("Terjadi kesalahan:", err)


# JALANKAN PROGRAM
if __name__ == "__main__":
    main()