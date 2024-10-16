inventory = {}

def display_menu():
    print("\n=== Menu Inventory ===")
    print("1. Menambah barang")
    print("2. Menghapus barang")
    print("3. Menampilkan daftar barang")
    print("4. Mencari barang")
    print("5. Mengupdate data barang")
    print("6. Keluar")

def tambah_barang():
    kode = input("Masukkan kode barang: ").upper()
    if kode in inventory:
        print("kode barang tersebut sudah ada")
    else:
        nama = input("Masukkan nama barang: ")
        jumlah = int(input("Masukkan jumlah barang: "))
        harga = float(input("Masukan harga barang: "))
        inventory[kode] = {'nama': nama, 'jumlah': jumlah, 'harga': harga}
        print(f"barang {nama} berhasil ditambahkan")

def hapus_barang():
    kode = input("Masukkan kode barang yang mau dihapus: ").upper()
    if kode in inventory:
        del inventory[kode]
        print(f"Barang dengan kode {kode} tersebut berhasil dihapus")
    else:
        print("Barang tidak ditemukan")


def tampilkan_barang():
    if not inventory:
        print("Inventory kosong")
    else:
        print("\n=== Daftar barang ===")
        for kode, data in inventory.items():
            print(f"kode: {kode}, nama: {data['nama']}, jumlah: {data['jumlah']}, harga: {data['harga']}")

def cari_barang():
    kode = input("Masukan kode barang yang mau dicari: ").upper()
    if kode in inventory:
        data = inventory[kode]
        print(f"kode: {kode}, nama: {data['nama']}, jumlah: {data['jumlah']}, harga: {data['harga']}")
    else:
        print("Barang tidak ditemukan")

def update_barang():
    kode = input ("Masukkan kode barang yang ingin di-update: ").upper()
    if kode in inventory:
        print(f"Barang ditemukan: {inventory[kode]}")
        nama_baru = input("Masukkan nama barang baru: ")
        jumlah_baru = input("Masukkan jumlah barang baru: ")
        harga_baru = input("Masukkan harga barang baru: ")

        if nama_baru:
            inventory[kode]['nama'] = nama_baru
        elif jumlah_baru:
            inventory[kode]['jumlah'] = int(jumlah_baru)
        elif harga_baru:
            inventory[kode]['harga'] = float(harga_baru)
        print("Data barang berhasil diperbaharui")
    else:
        print("Barang tidak ditemukan")

def main():
    while True:
        display_menu()
        pilihan = input("Silahkan pilih menu (1-6): ")
        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            hapus_barang()
        elif pilihan == '3':
            tampilkan_barang()
        elif pilihan == '4':
            cari_barang()
        elif pilihan == '5':
            update_barang()
        elif pilihan == '6':
            print("Terima kasih telah menggunakan program ini")
            break
        else:
            print("Pilihan tidak valid, coba lagi")

main()