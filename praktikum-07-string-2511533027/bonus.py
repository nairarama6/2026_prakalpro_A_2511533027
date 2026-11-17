# Nama: Naira Ramadhani Halil
# NIM: 2511533027
# Question Bonus

kalimat = "Mie ayam itu enak"
bersih = kalimat.lower().replace(" ", "")
dibalik = bersih[::-1]
if bersih == dibalik:
    print("Palindrome")
else:
    print("Not a palindrome")