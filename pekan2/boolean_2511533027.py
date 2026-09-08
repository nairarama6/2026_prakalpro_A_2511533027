is_lulus_3027 = True
is_cumlaude_3027 = True

#Menggunakan Boolean
nilai_3027 = 85
batas_lulus_3027 = 75

#Menentukan nilai Boolean dari kondisi
status_kelulusan_3027 = nilai_3027 >= batas_lulus_3027 # Hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai:", nilai_3027)
print("Apakah lulus?:", status_kelulusan_3027)
if is_lulus_3027 and is_cumlaude_3027:
    print("Selamat, Anda lulus dengan predikat Cumlaude!")