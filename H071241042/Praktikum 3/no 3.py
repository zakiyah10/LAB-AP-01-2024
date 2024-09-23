# n = int(input("Masukkan jumlah baris (N): ")) 
# m = int(input("Masukkan jumlah kolom (M): ")) 
 
# for i in range(n): 
#     if i % 2 == 0: 
#         for j in range(m): 
#             print(f"MOVE ke ({i}, {j})") 
#     else: 
#         for j in range(m -1, -1, -1): 
#             print(f"MOVE ke ({i}, {j})")
n = int(input("Masukkan jumlah baris (N): "))
m = int(input("Masukkan jumlah kolom (M): "))

# Jika n atau m negatif, ubah menjadi positif dan ubah arah gerakan
if n < 0:
    n = -n
    arah_baris = -1
else:
    arah_baris = 1

if m < 0:
    m = -m
    arah_kolom = -1
else:
    arah_kolom = 1

for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            print(f"MOVE ke ({i * arah_baris}, {j * arah_kolom})")
    else:
        for j in range(m - 1, -1, -1):
            print(f"MOVE ke ({i * arah_baris}, {j * arah_kolom})")