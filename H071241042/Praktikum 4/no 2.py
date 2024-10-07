def harta_karun():
    total_jarak = 0
    bahaya = 'tidak'
    while True:
        try:
            jarak_langkah = int(input("Masukkan langkah (meter) atau 0 untuk selesai: "))
        except:
            print("Input tidak valid. Masukkan bilangan bulat ")
            break
            
        total_jarak += jarak_langkah
        if jarak_langkah > 20:
            bahaya = "Ya"

        def keputusan():
            print(f"Total jarak: {total_jarak} meter")
            if bahaya == "Ya":
                keputusan_akhir = "Tidak aman untuk menggali!"
            elif total_jarak != 50:
                keputusan_akhir = "Harta tidak ditemukan!"
            else:
                keputusan_akhir = "Aman! Kamu tepat menemukan harta karun dan menang!"
            print(f"Ada bahaya: {bahaya}")
            print(f"Keputusan: {keputusan_akhir}")
            
        if jarak_langkah == 0:
            keputusan()
            break

harta_karun()