def Palindrome(s):
    clean_s = ''.join(s.split()).lower()
    
    if clean_s == clean_s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"
print(Palindrome("Ibu  Ratna Antar   Ubi"))  
print(Palindrome("Sistem Informasi 2024"))