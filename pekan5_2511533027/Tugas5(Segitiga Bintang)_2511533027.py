tinggi_3027 = int(input("Masukkan tinggi segitiga: "))

for i_3027 in range(1, tinggi_3027 + 1):

    # Membuat spasi di sebelah kiri
    for j_3027 in range(tinggi_3027 - i_3027):
        print(" ", end=" ")

    # Membuat segitiga penuh
    for j_3027 in range(1, (2 * i_3027)):
        print("*", end=" ")

    print()