print("\n================================")
print("3. OPERATOR BITWISE")
print("================================")

angka1_3027 = int(input("Masukkan angka bitwise-1: "))
angka2_3027 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan binner")
print("angka1 =", angka1_3027, "| biner =", bin(angka1_3027))
print("angka2 =", angka2_3027, "| biner =", bin(angka2_3027))

#Bitwise AND
hasil = angka1_3027 & angka2_3027
print("\nBitwise AND (&)")
print(angka1_3027, "&", angka2_3027, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

#Bitwise OR
hasil = angka1_3027 | angka2_3027
print("\nBitwise OR (|)")
print(angka1_3027, "|", angka2_3027, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

#Bitwise XOR
hasil = angka1_3027 ^ angka2_3027
print("\nBitwise XOR (^)")
print(angka1_3027, "^", angka2_3027, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

#Bitwise NOT
hasil = ~angka1_3027
print("\nBitwise NOT (~)")
print("~", angka1_3027, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))


#Bitwise geser kiri
jumlah_geser_3027 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil = angka1_3027 << jumlah_geser_3027
print("\nBitwise Geser Kiri (<<)")
print(angka1_3027, "<<", jumlah_geser_3027, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

#Bitwise geser kanan
hasil = angka1_3027 >> jumlah_geser_3027
print("\nBitwise Geser Kanan (>>)")
print(angka1_3027, ">>", jumlah_geser_3027, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))