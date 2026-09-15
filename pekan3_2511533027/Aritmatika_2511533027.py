angka1_3027 = int(input("Input angka-1: "))
angka2_3027 = int(input("Input angka-2: "))

#Penjumlahan
hasil = angka1_3027 + angka2_3027
print("\nOperator Penjumlahan")
print("Hasil: ", hasil)

#Pengurangan
hasil = angka1_3027 - angka2_3027
print("\nOperator Pengurangan")
print("Hasil: ", hasil)

#Perkalian
hasil = angka1_3027 * angka2_3027
print("\nOperator Perkalian")
print("Hasil =", hasil)

#Pembagian, pembagian bulat, dan sisa bagi
if angka1_3027 !=0:
    hasil = angka1_3027 / angka2_3027
    print("\nOperator Pembagian")
    print("Hasil =", hasil)
    
    hasil = angka1_3027 // angka2_3027
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil)
    
    hasil = angka1_3027 % angka2_3027
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil)
    
else:
    print("Angka kedua tidak boleh bernilai 0.")
    
#Pangkat
hasil = angka1_3027 ** angka2_3027
print("\nOperator Pangkat")
print("Hasil =", hasil)