# Latihan Manipulasi List

# 1. Buat sebuah list sebanyak 5 elemen dengan nilai bebas
A = [10, 20, 30, 40, 50]
print("List A:", A)
print()

# 2. Akses list
print("=== AKSES LIST ===")
# Tampilkan elemen ke 3 (index 2)
print("Elemen ke-3:", A[2])

# Ambil nilai elemen ke 2 sampai elemen ke 4 (index 1 sampai 3)
print("Elemen ke-2 sampai ke-4:", A[1:4])

# Ambil elemen terakhir
print("Elemen terakhir:", A[-1])
print()

# 3. Ubah elemen list
print("=== UBAH ELEMEN LIST ===")
# Ubah elemen ke 4 (index 3)
A[3] = 99
print("Setelah ubah elemen ke-4:", A)

# Ubah elemen ke 4 sampai dengan elemen terakhir (index 3 ke akhir)
A[3:] = [100, 200]
print("Setelah ubah elemen ke-4 sampai akhir:", A)
print()

# 4. Tambah elemen list
print("=== TAMBAH ELEMEN LIST ===")
# Ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
B = A[0:2]  # Ambil 2 elemen pertama
print("List B (dari 2 elemen pertama A):", B)

# Tambah list B dengan nilai string
B.append("Python")
print("Setelah tambah string:", B)

# Tambah list B dengan 3 nilai
B.extend([60, 70, 80])
print("Setelah tambah 3 nilai:", B)

# Gabungkan list B dengan list A
A.extend(B)
print("List A setelah digabung dengan B:", A)
print()

print("=== HASIL AKHIR ===")
print("List A:", A)
print("List B:", B)