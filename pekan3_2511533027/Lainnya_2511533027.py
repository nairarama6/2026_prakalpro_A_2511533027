print("================================")
print("1. OPERATOR KEANGGOTAAN")
print("================================")

#Input beberapa data yang dipisahkan dengan koma
input_data_3027 = input("Input beberapa angka, pisahkan dengan koma: ")

#Mengubah input menjadi list integer
data_3027 = [int(angka.strip()) for angka in input_data_3027.split(",")]

nilai_dicari_3027 = int(input("Masukkan angka yang ingin dicari: "))

#Operator in
hasil = nilai_dicari_3027 in data_3027
print("\nOperator Keanggotaan IN")
print(nilai_dicari_3027, "in", data_3027, "=", hasil)

#Operator not in
hasil = nilai_dicari_3027 not in data_3027
print("\nOperator Keanggotaan NOT IN")
print(nilai_dicari_3027, "not in", data_3027, "=", hasil)

print("\n================================")
print("2. OPERATOR IDENTITAS")
print("================================")

#Objek1 menggunakan list dari input pengguna
objek1_3027 = data_3027

#Objek2 merujuk pada objek yang sama dengan objek1
objek2_3027 = objek1_3027

#Objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_3027 = data_3027.copy()

print("objek1 =", objek1_3027)
print("objek2 =", objek2_3027)
print("objek3 =", objek3_3027)

#Operator is
hasil = objek1_3027 is objek2_3027
print("\nOperator Identitas IS")
print("objek1 is objek2 =", hasil)

#Operator is not
hasil = objek1_3027 is not objek3_3027
print("\nOperator Identitas IS NOT")
print("objek1 is not objek3 =", hasil)

#Membandingkan identitas dan nilai
print("\nPerbandingan Identitas dan Nilai")
print("objek1 is objek3 =", objek1_3027 is objek3_3027)
print("objek1 == objek3 =", objek1_3027 == objek3_3027)