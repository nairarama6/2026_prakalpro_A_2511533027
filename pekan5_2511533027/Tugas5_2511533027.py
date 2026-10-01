print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

n_3027 = int(input("Masukkan ukuran skala jam pasir (N): "))

if n_3027 <= 0:
    print("N harus bilangan positif!")
else:
    # Border atas
    print("#", end="")

    for i_3027 in range(4 * n_3027 + 5):
        print("=", end="")

    print("#")

    # Fase 1: Jam Pasir Atas
    for baris_3027 in range(n_3027, 0, -1):
        print("|", end="")

        # Padding kiri
        print(" ", end="")
        for spasi_3027 in range(2 * (n_3027 - baris_3027)):
            print(" ", end="")

        # Angka menurun
        for angka_3027 in range(baris_3027, 0, -1):
            print(angka_3027, end=" ")

        # Poros kristal
        print("<*>", end="")

        # Angka menaik
        for angka_3027 in range(1, baris_3027 + 1):
            print(" ", end="")
            print(angka_3027, end="")

        # Padding kanan
        for spasi_3027 in range(2 * (n_3027 - baris_3027)):
            print(" ", end="")

        print(" |")

    # Fase 2: Poros titik pusat
    print("|", end="")

    for spasi_3027 in range(2 * n_3027 + 1):
        print(" ", end="")

    print("<*>", end="")

    for spasi_3027 in range(2 * n_3027 + 1):
        print(" ", end="")

    print("|")

    # Fase 3: Jam Pasir Bawah
    for baris_3027 in range(1, n_3027 + 1):
        print("|", end="")

        # Padding kiri
        print(" ", end="")
        for spasi_3027 in range(2 * (n_3027 - baris_3027)):
            print(" ", end="")

        # Angka menurun
        for angka_3027 in range(baris_3027, 0, -1):
            print(angka_3027, end=" ")

        # Poros kristal
        print("<*>", end="")

        # Angka menaik
        for angka_3027 in range(1, baris_3027 + 1):
            print(" ", end="")
            print(angka_3027, end="")

        # Padding kanan
        for spasi_3027 in range(2 * (n_3027 - baris_3027)):
            print(" ", end="")

        print(" |")

    # Border bawah
    print("#", end="")

    for i_3027 in range(4 * n_3027 + 5):
        print("=", end="")

    print("#")