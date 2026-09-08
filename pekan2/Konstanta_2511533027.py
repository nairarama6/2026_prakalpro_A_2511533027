from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_3027 = float(input('Masukkan nilai jari-jari: '))
luas_3027 = PI * jari_3027 * jari_3027
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_3027, luas_3027))