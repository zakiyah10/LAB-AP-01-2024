import re

def validasi_ip(ip:str) -> str :
    ip4_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    ip6_pattern = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"

    if re.match(ip4_pattern, ip):
        parts = ip.split(".")
        if all(0 <= int(part) <= 255 for part in parts):
            return "IPv4"
    elif re.match(ip6_pattern, ip):
        return "IPv6"
    
    return "False"

def cek_ip(N: int, ip_addresses: list) :
    results = []
    for ip in ip_addresses[:N]: 
        results.append(validasi_ip(ip.strip()))
    return results

try :
    baris  = int(input("Masukkan jumlah baris IP = "))
    ip_addresses = [input(f"IP address {i+1}:  ") for i in range(baris)]
    resulst = cek_ip(baris, ip_addresses)

    for result in resulst:
        print(result)

except:
    print("Input tidak valid!")