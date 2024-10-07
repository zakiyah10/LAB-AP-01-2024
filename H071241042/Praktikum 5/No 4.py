def cetak_substring(s):
    n = len(s)
    for panjang in range(1, n + 1):
        for i in range(n - panjang + 1):
            print(s[i:i + panjang])

input_string = input("Masukkan sebuah string: ")
print('====================')
cetak_substring(input_string)
