# mengidentifikasi jenis segitiga berdasarkan panjang sisi-sisinya

sisi_pertama = float(input("Masukkan panjang sisi pertama: "))
sisi_kedua = float(input("Masukkan panjang sisi kedua: "))
sisi_ketiga = float(input("Masukkan panjang sisi ketiga: "))

# validasi input
if sisi_pertama <= 0 or sisi_kedua <= 0 or sisi_ketiga <= 0:
    print ("Inputan tidak valid")
elif sisi_pertama + sisi_kedua <= sisi_ketiga or sisi_pertama + sisi_ketiga <= sisi_kedua or sisi_kedua + sisi_ketiga <= sisi_pertama:
    print ("Tidak dapat membentuk segitiga yang valid")
else:
    # menentukan jenis segitiga
    if sisi_pertama == sisi_kedua and sisi_kedua == sisi_ketiga:
        print ("Segitiga Sama Sisi")
    elif sisi_pertama == sisi_kedua or sisi_pertama == sisi_ketiga or sisi_kedua == sisi_ketiga:
        print ("Segitiga Sama Kaki")
    else:
        print ("Segitiga Sembarang")
