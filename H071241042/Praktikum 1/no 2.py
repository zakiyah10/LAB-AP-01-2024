karakter = (input('Masukkan karakter :'))
kalimat = (input('Masukkan kalimat :'))


hasil_list = (f"{karakter} tidak terdapat dalam kalimat",f"{karakter} terdapat dalam kalimat")
hasil_index = ( karakter in kalimat)

hasil= hasil_list[hasil_index]
print(hasil)