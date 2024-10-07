def hitung_penghapusan_untuk_anagram(str1, str2):
   
    total_penghapusan = 0
    for char in set(str1 + str2):
        total_penghapusan += abs(str1.count(char) - str2.count(char))
    return total_penghapusan

str1 = input("Masukkan string pertama: ")
str2 = input("Masukkan string kedua: ")

hasil = hitung_penghapusan_untuk_anagram(str1, str2)
print(f"Jumlah minimum penghapusan karakter untuk membuat anagram: {hasil}")
