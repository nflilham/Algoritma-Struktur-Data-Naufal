# Naufal Ilham Fauzan
# 2502106
# Searching

"""Pencarian data: linear search dan binary search.

Time Complexity : linear O(n), binary O(log n)
Space Complexity: O(1)
"""


def linear_search(data: list[int], target: int) -> int:
    """Cari indeks target dengan menelusuri data satu per satu.

    Time Complexity : O(n)
    Space Complexity: O(1)
    """
    for i, nilai in enumerate(data):
        if nilai == target:
            return i
    return -1


def binary_search(data: list[int], target: int) -> int:
    """Cari indeks target pada data terurut dengan membagi dua rentang.

    Data wajib sudah terurut menaik; hasil tidak dijamin bila tidak terurut.

    Time Complexity : O(log n)
    Space Complexity: O(1)
    """
    kiri = 0
    kanan = len(data) - 1

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if data[tengah] == target:
            return tengah
        if data[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    return -1


def main() -> None:
    data = [12, 7, 25, 3, 18, 7, 40]
    target = 18

    print(f"Data   : {data}")
    print(f"Target : {target}")

    indeks = linear_search(data, target)
    print(f"Linear search -> indeks {indeks}")

    data_urut = sorted(data)
    print(f"Data terurut  : {data_urut}")
    indeks = binary_search(data_urut, target)
    print(f"Binary search -> indeks {indeks}")


if __name__ == "__main__":
    # linear search
    assert linear_search([1, 2, 3], 2) == 1
    assert linear_search([1, 2, 3], 9) == -1        # edge case: tidak ada
    assert linear_search([], 5) == -1               # edge case: data kosong
    assert linear_search([4, 4], 4) == 0            # edge case: duplikat

    # binary search
    assert binary_search([1, 2, 3], 3) == 2
    assert binary_search([1, 2, 3], 0) == -1        # edge case: tidak ada
    assert binary_search([], 5) == -1               # edge case: data kosong
    assert binary_search([7], 7) == 0               # edge case: satu elemen
    assert binary_search([1, 3, 5, 7, 9], 1) == 0   # edge case: batas kiri
    assert binary_search([1, 3, 5, 7, 9], 9) == 4   # edge case: batas kanan

    print("Semua test lulus")
    main()
