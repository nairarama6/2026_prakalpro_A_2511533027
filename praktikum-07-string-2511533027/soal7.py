# Nama: Naira Ramadhani Halil
# NIM: 2511533027
# Question 7

name = "naira ramadhani halil"
nim = "2511533027"
username = "naira027"
intake = "20" + nim[:2]

print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")
print("=" * 30)