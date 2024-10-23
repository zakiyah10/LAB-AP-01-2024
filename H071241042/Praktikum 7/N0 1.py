import os
from datetime import datetime

if not os.path.exists("tickets"):
    os.makedirs("tickets")

daftar_film = []
tiket_terdaftar = []

def menu_utama():
    while True:
        print("\n=== Sistem Pemesanan Tiket Bioskop ===")
        print("1. Admin")
        print("2. Pengunjung")
        print("3. Keluar")
        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == "1":
            menu_admin()
        elif pilihan == "2":
            menu_pengunjung()
        elif pilihan == "3":
            print("Terima kasih kaka >.< !")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

def menu_admin():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Tambah Film")
        print("2. Hapus Film")
        print("3. Daftar Tiket")
        print("4. Kembali")
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            tambah_film()
        elif pilihan == "2":
            hapus_film()
        elif pilihan == "3":
            menu_daftar_tiket()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid.")

def tambah_film():
    # Cek apakah file films.txt sudah ada, jika belum buat file kosong
    if not os.path.exists("films.txt"):
        open("films.txt", "w").close()

    while True:
        print("\n=== Tambah Film ===")
        film = input("Masukkan nama film yang ingin ditambahkan (Enter untuk kembali): ")
        if film == "":
            break  
        else:
            daftar_film.append(film)
            with open("films.txt", "a") as file:
                file.write(f"{film}\n")
            print(f"Film '{film}' berhasil ditambahkan!")



def hapus_film():
    while True:
        print("\n=== Hapus Film ===")
        for i, film in enumerate(daftar_film):
            print(f"{i + 1}. {film}")
        print("0. Kembali")

        pilihan = input("Masukkan nomor film yang ingin dihapus: ")
        if pilihan == "0":
            break
        elif pilihan.isdigit() and 1 <= int(pilihan) <= len(daftar_film):
            film_terhapus = daftar_film.pop(int(pilihan) - 1)
            print(f"Film '{film_terhapus}' berhasil dihapus!")

            # Perbarui file films.txt
            with open("films.txt", "w") as file:
                for film in daftar_film:
                    file.write(f"{film}\n")
        else:
            print("Pilihan tidak valid.")


def menu_daftar_tiket():
    while True:
        print("\n=== Daftar Tiket ===")
        print("1. Lihat daftar tiket")
        print("2. Lihat detail tiket")
        print("3. Hapus tiket")
        print("4. Kembali")
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            lihat_daftar_tiket()
        elif pilihan == "2":
            lihat_detail_tiket()
        elif pilihan == "3":
            hapus_tiket()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid.")

def lihat_daftar_tiket():
    print("\nDaftar Tiket:")
    if not tiket_terdaftar:
        print("Belum ada tiket yang terdaftar.")
    else:
        for i, tiket in enumerate(tiket_terdaftar):
            print(f"{i + 1}. {tiket}")

def lihat_detail_tiket():
    lihat_daftar_tiket()
    pilihan = input("Pilih nomor tiket yang ingin dilihat detailnya: ")

    if pilihan.isdigit() and 1 <= int(pilihan) <= len(tiket_terdaftar):
        tiket = tiket_terdaftar[int(pilihan) - 1]
        tampilkan_tiket(tiket)
    else:
        print("Pilihan tidak valid.")

def hapus_tiket():
    lihat_daftar_tiket()
    pilihan = input("Pilih nomor tiket yang ingin dihapus: ")

    if pilihan.isdigit() and 1 <= int(pilihan) <= len(tiket_terdaftar):
        tiket = tiket_terdaftar.pop(int(pilihan) - 1)
        os.remove(f"tickets/{tiket}.txt")
        print(f"Tiket '{tiket}' berhasil dihapus.")
    else:
        print("Pilihan tidak valid.")

def menu_pengunjung():
    while True:
        print("\n=== Menu Pengunjung ===")
        print("1. Lihat daftar film")
        print("2. Beli Tiket")
        print("3. Kembali")
        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == "1":
            lihat_daftar_film()
        elif pilihan == "2":
            beli_tiket()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid.")

def lihat_daftar_film():
    print("\nDaftar Film:")
    
    # Cek apakah file films.txt ada
    if os.path.exists("films.txt"):
        # Baca film dari file
        with open("films.txt", "r") as file:
            daftar_film = file.readlines()
            daftar_film = [film.strip() for film in daftar_film]  # Menghapus karakter newline

        if daftar_film:
            for i, film in enumerate(daftar_film):
                print(f"{i + 1}. {film}")
        else:
            print("Belum ada film yang tersedia.")
    else:
        print("Belum ada film yang tersedia.")
    


def beli_tiket():
    lihat_daftar_film()
    pilihan = input("Pilih nomor film yang ingin ditonton: ")

    if pilihan.isdigit() and 1 <= int(pilihan) <= len(daftar_film):
        film = daftar_film[int(pilihan) - 1]
        id_tiket = buat_id_tiket()
        tiket_terdaftar.append(id_tiket)
        simpan_tiket(id_tiket, film)
        print(f"\nTiket berhasil dibeli. ID tiket anda: {id_tiket}")
        
    else:
        print("Pilihan tidak valid.")

def buat_id_tiket():
    waktu_sekarang = datetime.now().strftime("%d%m%Y%H%M%S")
    return f"TICK{waktu_sekarang}"

def simpan_tiket(id_tiket, film):
    tanggal = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with open(f"tickets/{id_tiket}.txt", "w") as file:
        file.write(
            "+-----------------------------------+\n"
            "|          TIKET BIOSKOP            |\n"
            "+-----------------------------------+\n"
            f"| ID Tiket : {id_tiket}             \n"
            f"| Film     : {film}                 \n"
            f"| Tanggal  : {tanggal}              \n"
            "+-----------------------------------+\n"
            "|    Terima Kasih Tentang Kembali   |\n"
            "|            tiket anda!            |\n"
            "+-----------------------------------+\n"
        )

def tampilkan_tiket(id_tiket):
    with open(f"tickets/{id_tiket}.txt", "r") as file:
        print(file.read())

menu_utama()
