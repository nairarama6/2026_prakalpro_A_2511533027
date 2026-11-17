# Nama: Naira Ramadhani Halil
# NIM: 2511533027
# Question 4

phone = "082511533027"
hidden_count = len(phone) - 7
masked = phone[:4] + "*" * hidden_count + phone[-3:]
print(masked)