def hitung_langkah(n):
        langkah = 0
        while n != 1 :
            if n % 2 == 0 :
                n = n/2
            else :
                n = n * 3 + 1
            langkah += 1
            print(n)
        return langkah

def main(): 
 try:
        n = int(input("Masukkan angka: "))
        if n <= 0:
            print("Input tidak Valid")
        else:
            langkah = hitung_langkah(n)
            print(f"Jumlah langkah: {langkah}")
 except ValueError:
       print("Input tidak Valid")

main()