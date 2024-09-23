import random

angka_rahasia = random.randint(1, 100)
kesempatan = 5

print("Saya telah memilih angka antara 1 dan 100. Coba tebak!")

while kesempatan > 0 or kesempatan == ValueError:
  
  print(f"Kesempatan tersisa: {kesempatan}")
  try:
    tebakan = int(input("Masukkan tebakan Anda (0 untuk berhenti): "))
  except ValueError:
    print("Input bukan angka")
    kesempatan -= 1
    continue

  if tebakan == 0:
    break

  if tebakan == angka_rahasia:
    print("Selamat! Anda menebak angka dengan benar.")
    break

  elif tebakan < angka_rahasia:
    print("Angka terlalu kecil.")
  else:
      if tebakan > angka_rahasia:
        print("Angka terlalu besar.")
      elif tebakan == ValueError:
        print("Input bukan angka.")

  kesempatan -= 1

if kesempatan == 0:
  print(f"Anda kehabisan kesempatan. Angka rahasianya adalah {angka_rahasia}")