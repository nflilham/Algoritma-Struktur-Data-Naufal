print("==============================")
print("      1. NUMBER TRIANGLE      ")
print("==============================")

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("==============================")
print("      2. FLOYD'S TRIANGLE     ")
print("==============================")

n = 5
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

print("==============================")
print(" 3. PALINDROME NUMBER PYRAMID ")
print("==============================")

n = 5
for i in range(1, n + 1):
    # print spaces
    print(" " * (n - i), end=" ")
    # increasing part
    for j in range(1, i + 1):
        print(j, end="")
    # decreasing part
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

print("==============================")
print(" 4. INVERTED NUMBER TRIANGLE  ")
print("==============================")

n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("==============================")
print("       5. NUMBER PYRAMID      ")
print("==============================")

n = 5
for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

print("==============================")
print("  6. DIAMOND NUMBER PATTERN   ")
print("==============================")

n = 4
# upper half
for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()
# lower half
for i in range(n - 1, 0, -1):
    for j in range(1, n - i + 1):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()

print("==============================")
print("   7. HOLLOW NUMBER PYRAMID   ")
print("==============================")

n = 5
for i in range(1, n + 1):
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == n:
            print(j if j <= i else 2 * i - j, end=" ")
        else:
            print(" ", end=" ")
    print()

print("==============================")
print("     8. PASCAL'S TRIANGLE     ")
print("==============================")

n = 5
for i in range(n):
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()

print("==============================")
print("  9. NUMBER DIAMOND PATTERN   ")
print("==============================")

n = 4
# upper half
for i in range(1, n + 1):
    for j in range(1, 2 * i):
        print(j if j <= i else 2 * i - j, end=" ")
    print()
# lower half
for i in range(n - 1, 0, -1):
    for j in range(1, 2 * i):
        print(j if j <= i else 2 * i - j, end=" ")
    print()

print("==============================")
print(" 10. NUMBER HOURGLASS PATTERN ")
print("==============================")

n = 3
# upper half
for i in range(n, 0, -1):
    # spaces
    for j in range(n - i):
        print(" ", end=" ")
    # increasing part
    for j in range(1, i + 1):
        print(j, end=" ")
    # decreasing part
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()
# lower half
for i in range(2, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()

print("===================================")
print(" 11. RIGHT ALIGNED NUMBER TRIANGLE ")
print("===================================")

n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("==============================")
print("   12. NUMBER HILL PATTERN    ")
print("==============================")

n = 4
for i in range(1, n + 1):
    # spaces
    for j in range(n - i):
        print(" ", end=" ")
    # increasing part
    for j in range(1, i + 1):
        print(j, end=" ")
    # decreasing part
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()

print("==============================")
print(" 13. Butterfly Number Pattern ")
print("==============================")

n = 5
# upper half
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(2 * (n - i)):
        print(" ", end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
# lower half
for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(2 * (n - i)):
        print(" ", end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

print("==============================")
print("     14. Number X Pattern     ")
print("==============================")

n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == i or j == n - i + 1:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()

print("==============================")
print("   15. Number Cross Pattern   ")
print("==============================")

n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == (n + 1) // 2 or j == (n + 1) // 2:
            print(1, end=" ")
        else:
            print(" ", end=" ")
    print()

print("==============================")
print("    16. Sandglass Pattern     ")
print("==============================")

n = 5
# upper half
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# lower half
for i in range(2, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("==============================")
print("   17. Number Spiral Pattern  ")
print("==============================")

n = 5
mat = [[0] * n for _ in range(n)]
top, bottom, left, right = 0, n - 1, 0, n - 1
num = 1
while top <= bottom and left <= right:
    # left to right
    for i in range(left, right + 1):
        mat[top][i] = num
        num += 1
    top += 1
    # top to bottom
    for i in range(top, bottom + 1):
        mat[i][right] = num
        num += 1
    right -= 1
    # right to left
    for i in range(right, left - 1, -1):
        mat[bottom][i] = num
        num += 1
    bottom -= 1
    # bottom to top
    for i in range(bottom, top - 1, -1):
        mat[i][left] = num
        num += 1
    left += 1

for i in range(n):
    for j in range(n):
        print(f"{mat[i][j]:2}", end=" ")
    print()

print("==============================")
print("        18. Z Pattern         ")
print("==============================")

n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or i + j == n - 1:
            print(j + 1, end=" ")
        else:
            print(" ", end=" ")
    print()