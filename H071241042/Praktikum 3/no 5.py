# Inisialisasi populasi awal
populasi_a = int(input("Masukkan populasi awal Serangga A: "))
populasi_b = int(input("Masukkan populasi awal Serangga B: "))
jumlah_hari = int(input("Masukkan jumlah hari: "))

# Simulasi pertumbuhan populasi
for hari in range(1, jumlah_hari + 1):

  # Pertumbuhan pada hari ganjil
  if hari % 2 != 0:
    populasi_a = int(populasi_a * 1.3)
    populasi_b = int(populasi_b * 1.5)
  # Pertumbuhan pada hari genap
  else:
    populasi_a = int(populasi_a * 0.8)
    populasi_b = int(populasi_b * 0.6)

  # Predator datang setiap kelipatan 5 hari
  if hari % 5 == 0:
    print(f"Hari {hari}: Predator memakan 10% populasi.")
    populasi_a = int(populasi_a * 0.9)
    populasi_b = int(populasi_b * 0.9)

  # Cetak populasi setiap hari
  print(f"Hari {hari}: Serangga A = {populasi_a}, Serangga B = {populasi_b}")
  if populasi_a < 1 and populasi_b < 1:
    break