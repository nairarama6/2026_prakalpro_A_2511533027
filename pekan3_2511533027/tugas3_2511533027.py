print("========================================")
print("       SISTEM TRANSAKSI TOKO")
print("========================================")

# INPUT DATA PELANGGAN
nama_3027 = input("Masukkan Nama Pelanggan : ")
status_3027 = input("Masukkan Status Pelanggan (member/nonmember) : ").lower()
total_belanja_3027 = int(input("Masukkan Total Belanja : Rp"))
jumlah_barang_3027 = int(input("Masukkan Jumlah Barang : "))
kode_promo_3027 = input("Masukkan Kode Promo : ").upper()

# DATA PROMO
daftar_promo_3027 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

# OPERATOR PERBANDINGAN
syarat_belanja_3027 = total_belanja_3027 >= 200000
syarat_barang_3027 = jumlah_barang_3027 >= 3
status_member_3027 = status_3027 == "member"

# OPERATOR KEANGGOTAAN
promo_tersedia_3027 = kode_promo_3027 in daftar_promo_3027
promo_tidak_tersedia_3027 = kode_promo_3027 not in daftar_promo_3027

# OPERATOR LOGIKA
diskon_member_3027 = status_member_3027 and syarat_belanja_3027

promo_3027 = syarat_barang_3027 and promo_tersedia_3027

hak_akses_3027 = (
    diskon_member_3027
    or promo_3027
)

bukan_member_3027 = not status_member_3027

# OPERATOR ARITMATIKA
diskon_3027 = 0

if diskon_member_3027:
    diskon_3027 = total_belanja_3027 * 10 / 100

total_pembayaran_3027 = total_belanja_3027 - diskon_3027

rata_rata_3027 = total_belanja_3027 / jumlah_barang_3027

sisa_bagi_3027 = total_belanja_3027 % jumlah_barang_3027

# OPERATOR PENUGASAN
poin_3027 = 0
poin_3027 += jumlah_barang_3027

if diskon_member_3027:
    poin_3027 += 10

total_pembayaran_3027 -= 0

# OPERATOR IDENTITY
objek_status_3027 = status_3027
status_sama_3027 = objek_status_3027 is status_3027
status_tidak_sama_3027 = objek_status_3027 is not status_3027

nilai_a_3027 = 100
nilai_b_3027 = 100
nilai_sama_3027 = nilai_a_3027 == nilai_b_3027

# OPERATOR BITWISE
kode_member_3027 = 1       # 0001
kode_belanja_3027 = 2      # 0010
kode_barang_3027 = 4       # 0100
kode_promo_bit_3027 = 8    # 1000

kode_status_3027 = 0

if status_member_3027:
    kode_status_3027 = kode_status_3027 | kode_member_3027

if syarat_belanja_3027:
    kode_status_3027 = kode_status_3027 | kode_belanja_3027

if syarat_barang_3027:
    kode_status_3027 = kode_status_3027 | kode_barang_3027

if promo_tersedia_3027:
    kode_status_3027 = kode_status_3027 | kode_promo_bit_3027


# AND (&)
cek_member_3027 = kode_status_3027 & kode_member_3027
cek_promo_3027 = kode_status_3027 & kode_promo_bit_3027

# XOR (^)
kode_referensi_3027 = 11
hasil_xor_3027 = kode_status_3027 ^ kode_referensi_3027

# SHIFT (<<)
hasil_shift_3027 = kode_status_3027 << 1

# HAK AKSES
member_access_3027 = cek_member_3027 == 1
promo_access_3027 = cek_promo_3027 == 8
free_shipping_access_3027 = promo_3027 and promo_tersedia_3027

# OUTPUT DATA
print("\n========================================")
print("           DATA PELANGGAN")
print("========================================")
print("Nama Pelanggan       :", nama_3027)
print("Status Pelanggan     :", status_3027)
print("Total Belanja        : Rp", total_belanja_3027)
print("Jumlah Barang        :", jumlah_barang_3027)
print("Kode Promo           :", kode_promo_3027)


print("\n========================================")
print("          HASIL VALIDASI")
print("========================================")
print("Belanja >= Rp200000  :", syarat_belanja_3027)
print("Jumlah Barang >= 3   :", syarat_barang_3027)
print("Status Member        :", status_member_3027)
print("Kode Promo Tersedia  :", promo_tersedia_3027)
print("Kode Promo Tidak Ada :", promo_tidak_tersedia_3027)
print("Mendapat Diskon      :", diskon_member_3027)
print("Mendapatkan Promo    :", promo_3027)


print("\n========================================")
print("          HASIL PERHITUNGAN")
print("========================================")
print("Besarnya Diskon      : Rp", int(diskon_3027))
print("Total Pembayaran     : Rp", int(total_pembayaran_3027))
print("Rata-rata Harga      : Rp", int(rata_rata_3027))
print("Sisa Pembagian       :", sisa_bagi_3027)
print("Jumlah Poin          :", poin_3027)


print("\n========================================")
print("        HAK AKSES PELANGGAN")
print("========================================")
print("Kode Hak Akses       :", format(kode_status_3027, "04b"))
print("Member Access        :", member_access_3027)
print("Promo Access         :", promo_access_3027)
print("Free Shipping Access :", free_shipping_access_3027)


print("\n========================================")
print("          HASIL OPERATOR")
print("========================================")

print("\n--- OPERATOR ARITMATIKA ---")
print("Diskon = Total Belanja * 10 / 100")
print("Total Pembayaran = Total Belanja - Diskon")
print("Rata-rata = Total Belanja / Jumlah Barang")
print("Sisa = Total Belanja % Jumlah Barang")

print("\n--- OPERATOR PERBANDINGAN ---")
print("Total Belanja >= 200000 :", syarat_belanja_3027)
print("Jumlah Barang >= 3      :", syarat_barang_3027)
print("Status == member        :", status_member_3027)

print("\n--- OPERATOR LOGIKA ---")
print("Member AND Belanja      :", diskon_member_3027)
print("Barang AND Promo        :", promo_3027)
print("Diskon OR Promo         :", hak_akses_3027)
print("NOT Member              :", bukan_member_3027)

print("\n--- OPERATOR PENUGASAN ---")
print("Poin += Jumlah Barang   :", poin_3027)
print("Pembayaran -= 0         :", int(total_pembayaran_3027))

print("\n--- OPERATOR KEANGGOTAAN ---")
print("Kode Promo IN daftar    :", promo_tersedia_3027)
print("Kode Promo NOT IN daftar:", promo_tidak_tersedia_3027)

print("\n--- OPERATOR IDENTITAS ---")
print("Objek status IS status  :", status_sama_3027)
print("Objek status IS NOT    :", status_tidak_sama_3027)
print("100 == 100             :", nilai_sama_3027)

print("\n--- OPERATOR BITWISE ---")
print("Kode Status             :", format(kode_status_3027, "04b"))
print("Kode Desimal            :", kode_status_3027)

print("\nCek Member:")
print(format(kode_status_3027, "04b"), "&", format(kode_member_3027, "04b"))
print("Hasil Biner             :", format(cek_member_3027, "04b"))
print("Hasil Desimal           :", cek_member_3027)

print("\nCek Promo:")
print(format(kode_status_3027, "04b"), "&", format(kode_promo_bit_3027, "04b"))
print("Hasil Biner             :", format(cek_promo_3027, "04b"))
print("Hasil Desimal           :", cek_promo_3027)

print("\nPerbandingan Status:")
print("Kode Transaksi          :", format(kode_status_3027, "04b"))
print("Kode Referensi          :", format(kode_referensi_3027, "04b"))
print(format(kode_status_3027, "04b"), "^", format(kode_referensi_3027, "04b"))
print("Hasil Biner             :", format(hasil_xor_3027, "04b"))
print("Hasil Desimal           :", hasil_xor_3027)

print("\nShift:")
print(format(kode_status_3027, "04b"), "<< 1")
print("Hasil Biner             :", format(hasil_shift_3027, "b"))
print("Hasil Desimal           :", hasil_shift_3027)

print("\n========================================")
print("              SELESAI")
print("========================================")