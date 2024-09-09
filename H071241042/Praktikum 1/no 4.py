suhu_celcius = int(input("Masukkan Suhu dalam Celcius: "))

Suhu_kelvin =suhu_celcius + 273.15
suhu_Reamur = suhu_celcius * 4/5
suhu_fahrenheit = suhu_celcius * 9/5 + 32

print(f"hasil dari suhu {suhu_celcius} Celcius ke Kelvin adalah : {Suhu_kelvin: .0f}K")
print(f"hasil dari suhu {suhu_celcius} Celcius ke Reamur adalah : {suhu_Reamur: .0f}R")
print(f"hasil dari suhu {suhu_celcius} Celcius ke Fahrenheit adalah : {suhu_fahrenheit: .0f}F")