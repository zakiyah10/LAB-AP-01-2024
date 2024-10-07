def is_chipher(text, pergeseran):
    huruf_kecil = "abcdefghijklmnopqrstuvwxyz"
    huruf_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    perubahan_text = ""

    for karakter in text :
        if karakter in huruf_kecil :
            indeks = huruf_kecil.index(karakter)
            indeks_baru = (indeks + pergeseran) % 26
            perubahan_text += huruf_kecil[indeks_baru]
        elif karakter in huruf_besar:
            indeks = huruf_besar.index(karakter)
            indeks_baru = (indeks + pergeseran) % 26  
            teks_terenkripsi += huruf_besar[indeks_baru]
        else: 
            perubahan_text += karakter

    print(f"Teks: {text}")
    print(f"Pergeseran: {pergeseran}")
    print(f"hasil perubahan: {perubahan_text}")


text = input("masukkan string = ")
pergeseran = int(input("masukkan jumlah pergeseran = "))
is_chipher(text, pergeseran)

