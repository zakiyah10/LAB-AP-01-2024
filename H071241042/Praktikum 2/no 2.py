# menghitung harga tiket masuk ke sebuah wahana bermain

usia = int(input("Masukkan usia: "))
if usia <= 0:
    print("Inputan tidak valid")
elif usia < 5:
    harga = 0
    print(f"Harga tiket: Rp. {int(harga)}")
else:
    status = input("Apakah Anda anggota (ya/tidak): ")
    if usia <= 12:
        harga = 50000        
    elif usia <= 59:
        harga = 100000
    else:
        harga = 70000
    hasil = harga - ((harga*20) / 100) if status == "ya" else harga
    print(f"Harga tiket: Rp. {int(hasil)}")
