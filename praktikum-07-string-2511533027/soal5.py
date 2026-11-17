# Nama: Naira Ramadhani Halil
# NIM: 2511533027
# Question 5

# A
username = input("Username: ")
if len(username) < 5:
    print("Invalid: Username minimal 5 karakter.")
elif not username.isalnum():
    print("Invalid: Username hanya huruf dan angka.")
elif not username[0].isalpha():
    print("Invalid: Username harus diawali huruf.")
else:
    print("Valid")
    
# B
nim = input("NIM: ")
if len(nim) == 10 and nim.isdigit():
    print(f"Valid: intake year 20{nim[:2]}")
else:
    print("Invalid NIM")