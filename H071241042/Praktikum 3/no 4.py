# Input total harga dan uang yang diberikan
total_harga = int(input("Masukkan total harga: "))
uang_diberikan = int(input("Masukkan uang yang diberikan: "))

# Hitung kembalian
kembalian = uang_diberikan - total_harga

# Definisikan pecahan uang
pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

# Hitung dan tampilkan rincian kembalian
if total_harga > uang_diberikan:
  print("Uang anda kurang")
  exit()

print("Output:")
for pecahan in pecahan_uang:
  jumlah_lembar = kembalian // pecahan
  if jumlah_lembar > 0:
    print(f"{jumlah_lembar} lembar Rp {pecahan:,}")
    kembalian %= pecahan 