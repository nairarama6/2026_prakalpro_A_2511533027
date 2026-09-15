a1_3027 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_3027 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 =", a1_3027)
print("A2 =", a2_3027)

#Konjungsi, bernilai true jika keduanya true
hasil = a1_3027 and a2_3027
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil)

#Disjungsi bernilai true jika salah satunya true
hasil = a1_3027 or a2_3027
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil)

#Negasi A1: membalik niLai A2
hasil = not a1_3027
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil)

#Negasi A2: membalik Nilai A2
hasil = not a2_3027
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil)

#XOR: bernilai true jika kedua nilai berbeda
hasil = a1_3027 != a2_3027
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil)