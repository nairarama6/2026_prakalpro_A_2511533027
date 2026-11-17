# Nama: Naira Ramadhani Halil
# NIM: 2511533027
# Question 4

# A
text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

# B
text = "Naira Ramadhani Halil"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)