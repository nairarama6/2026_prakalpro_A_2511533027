ulang_3027 = int(input("Masukkan jumlah perulangan: "))

jumlah_3027 = 0
for i_3027 in range(1, ulang_3027 + 1):
    print(i_3027, end=" ")
    jumlah_3027 = jumlah_3027 + i_3027
    
    if i_3027 < ulang_3027:
        print(" + ", end="")
    else:
        print(" = ", jumlah_3027, end="")
print()
print("Jumlah =", jumlah_3027)