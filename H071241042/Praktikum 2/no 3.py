# menentukan kelulusan mahasiswa

nilai_akhir = int(input("Masukkan nalai akhir: "))
if nilai_akhir > 100:
    predikat = "Tidak valid"
elif nilai_akhir < 0:
    predikat = "Tidak valid"
else:
    persentase_kehadiran = int(input("Masukkan persentase kehadiran: "))

    if 85 <= nilai_akhir <= 100 and persentase_kehadiran >= 75:
        predikat = "A"
    elif 70 <= nilai_akhir <= 84 and persentase_kehadiran >= 75:
        predikat = "B"
    elif 60 <= nilai_akhir <= 69 and persentase_kehadiran >= 75:
        predikat = "C"
    else:
        predikat = "Tidak lulus" 

print(f'Lulus dengan predikat: {predikat}')