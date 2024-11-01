import re

def validasi_string(s):
    if len(s) != 45:
        return "False"

    pattern1 = r'^[A-Za-z02468\s]{40}$'
    if not re.match(pattern1, s[:40]):
        return "40 karakter pertama harus terdiri dari huruf atau digit genap."

    pattern2 = r'^[13579\s]{5}$'
    if not re.match(pattern2, s[40:]):
        return "5 karakter terakhir harus terdiri dari digit ganjil atau whitespace."

    return "True"

string = input("Masukkan string yang ingin divalidasi: ")
result = validasi_string(string)
print(result)