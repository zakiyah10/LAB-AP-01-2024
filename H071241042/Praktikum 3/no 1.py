try:
    n = int(input("Masukkan jumlah baris: "))
    if n < 3:
        print("Input tidak valid")
        exit()
except ValueError:
    print("Input bukan angka")
    exit()

for i in range(n+1):
    if i % 2 != 1 :
        continue
    bintang = "* "*i
    hasil = bintang.center(n*3," ")
    print(hasil)

for i in range(n-1, -1, -1):
    if i % 2 == 0 :
        continue
    bintang = "* "*i
    hasil = bintang.center(n*3, " ")
    print(hasil)
