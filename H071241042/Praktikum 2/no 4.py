# menentukan paket data yang paling sesuai untuk pelanggan

data = int(input("Masukkan jumlah data yang digunakan (GB): "))
penggunaan = input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)? ")
pengguna = input("Apakah Anda pengguna Personal atau Bisnis? ")

if data < 10 and penggunaan == "off-peak" and pengguna == "personal" :
    paket = "Paket A"
elif 10 <= data <= 50 and penggunaan == "peak" and pengguna == "personal" :
    paket = "Paket B"
elif data > 50 and penggunaan == "peak":
    paket = "Paket C"
elif data > 50 and penggunaan == "off-peak":
    paket = "Paket D"
else :
    paket = "Tidak ada paket yang cocok"

print(f"Paket yang sesuai : {paket}")