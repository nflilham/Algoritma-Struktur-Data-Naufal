def judul(teks):
    print("=" * 40)
    print(teks.center(40))
    print("=" * 40)
 
 
# 1. NUMBER TRIANGLE (rata tengah)
judul("1. NUMBER TRIANGLE")
n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
 
# 2. FLOYD'S TRIANGLE (rata tengah)
judul("2. FLOYD'S TRIANGLE")
n = 5
num = 1
baris_list = []
for i in range(1, n + 1):
    angka = []
    for j in range(i):
        angka.append(str(num))
        num += 1
    baris_list.append(" ".join(angka))
lebar = len(baris_list[-1])
for baris in baris_list:
    print(baris.center(lebar).rstrip())
 
# 3. PALINDROME NUMBER PYRAMID (kode PDF sudah benar)
judul("3. PALINDROME NUMBER PYRAMID")
n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
 
# 4. INVERTED NUMBER TRIANGLE (rata tengah)
judul("4. INVERTED NUMBER TRIANGLE")
n = 5
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
 
# 5. NUMBER PYRAMID (spasi 2 per tingkat, karena tiap angka = 2 karakter)
judul("5. NUMBER PYRAMID")
n = 5
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()
 
# 6. DIAMOND NUMBER PATTERN (angka berlanjut: 1 / 2 3 2 / 4 5 6 5 4)
judul("6. DIAMOND NUMBER PATTERN")
n = 3
def baris_diamond(i):
    s = i * (i - 1) // 2 + 1          # angka awal baris ke-i
    print("  " * (n - i), end="")
    for j in range(s, s + i):
        print(j, end=" ")
    for j in range(s + i - 2, s - 1, -1):
        print(j, end=" ")
    print()
for i in range(1, n + 1):             # upper half
    baris_diamond(i)
for i in range(n - 1, 0, -1):         # lower half
    baris_diamond(i)
 
# 7. HOLLOW NUMBER PYRAMID
judul("7. HOLLOW NUMBER PYRAMID")
n = 5
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == n:
            print(j if j <= i else 2 * i - j, end=" ")
        else:
            print(" ", end=" ")
    print()
 
# 8. PASCAL'S TRIANGLE (rata tengah)
judul("8. PASCAL'S TRIANGLE")
n = 5
for i in range(n):
    print(" " * (n - 1 - i), end="")
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()
 
# 9. NUMBER DIAMOND PATTERN
judul("9. NUMBER DIAMOND PATTERN")
n = 4
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, 2 * i):
        print(j if j <= i else 2 * i - j, end=" ")
    print()
for i in range(n - 1, 0, -1):
    print("  " * (n - i), end="")
    for j in range(1, 2 * i):
        print(j if j <= i else 2 * i - j, end=" ")
    print()
 
# 10. NUMBER HOURGLASS PATTERN
judul("10. NUMBER HOURGLASS PATTERN")
n = 3
for i in range(n, 0, -1):             # upper half (menyempit)
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()
for i in range(2, n + 1):             # lower half (melebar)
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()
 
# 11. RIGHT ALIGNED NUMBER TRIANGLE
judul("11. RIGHT ALIGNED NUMBER TRIANGLE")
n = 5
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
 
# 12. NUMBER HILL PATTERN
judul("12. NUMBER HILL PATTERN")
n = 4
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()
 
# 13. BUTTERFLY NUMBER PATTERN (kiri naik, jeda spasi, kanan turun)
judul("13. BUTTERFLY NUMBER PATTERN")
n = 5
for i in list(range(1, n + 1)) + list(range(n - 1, 0, -1)):
    for j in range(1, i + 1):
        print(j, end=" ")
    print(" " * (4 * (n - i)), end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
 
# 14. NUMBER X PATTERN
judul("14. NUMBER X PATTERN")
n = 5
for i in range(1, 2 * n):
    v = i if i <= n else 2 * n - i
    for j in range(1, 2 * n):
        if j == v or j == 2 * n - v:
            print(v, end=" ")
        else:
            print(" ", end=" ")
    print()
 
# 15. NUMBER CROSS PATTERN (kode PDF sudah benar)
judul("15. NUMBER CROSS PATTERN")
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == (n + 1) // 2 or j == (n + 1) // 2:
            print(1, end=" ")
        else:
            print(" ", end=" ")
    print()
 
# 16. SANDGLASS PATTERN (rata tengah)
judul("16. SANDGLASS PATTERN")
n = 5
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
for i in range(2, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
 
# 17. NUMBER SPIRAL PATTERN (kolom dirapikan agar angka 2 digit sejajar)
judul("17. NUMBER SPIRAL PATTERN")
n = 5
mat = [[0] * n for _ in range(n)]
top, bottom, left, right = 0, n - 1, 0, n - 1
num = 1
while top <= bottom and left <= right:
    for i in range(left, right + 1):
        mat[top][i] = num; num += 1
    top += 1
    for i in range(top, bottom + 1):
        mat[i][right] = num; num += 1
    right -= 1
    for i in range(right, left - 1, -1):
        mat[bottom][i] = num; num += 1
    bottom -= 1
    for i in range(bottom, top - 1, -1):
        mat[i][left] = num; num += 1
    left += 1
for i in range(n):
    for j in range(n):
        print(f"{mat[i][j]:<3}", end="")
    print()
 
# 18. Z PATTERN (kode PDF sudah benar)
judul("18. Z PATTERN")
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or i + j == n - 1:
            print(j + 1, end=" ")
        else:
            print(" ", end=" ")
    print()