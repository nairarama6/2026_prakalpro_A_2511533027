angka1_3027 = int(input("Input angka-1: "))
angka2_3027 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =", angka1_3027)
print("Nilai angka2 =", angka2_3027)

#Assignment biasa
hasil = angka1_3027
print("\nAssignment Biasa (=)")
print("Hasil =", hasil)

#Assignment penambahan
hasil = angka1_3027
hasil += angka2_3027
print("\nAssignment Penambahan (+=)")
print("Hasil =", hasil)

#Assignment pengurangan
hasil = angka1_3027
hasil -= angka2_3027
print("\nAssignment Pengurangan (-=)")
print("Hasil =", hasil)

#Assignment perkalian
hasil = angka1_3027
hasil *= angka2_3027
print("\nAssignment Perkalian (*=)")
print("Hasil =", hasil)

#Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_3027 != 0:
    hasil = angka1_3027
    hasil /= angka2_3027
    print("\nAssignment Pembagian (/=)")
    print("Hasil =", hasil)
    
    #Operator tambahan
    hasil = angka1_3027
    hasil //= angka2_3027
    print("\nAssignment Pembagian Bulat (//=)")
    print("Hasil =", hasil)
    
    hasil = angka1_3027
    hasil %= angka2_3027
    print("\nAssignment Sisa Bagi (%=)")
    print("Hasil =", hasil)
    
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")
    
#Operator tambahan: assignment perpangkatan
hasil = angka1_3027
hasil **= angka2_3027
print("\nAssignment Perpangkatan (**=)")
print("Hasil =", hasil)