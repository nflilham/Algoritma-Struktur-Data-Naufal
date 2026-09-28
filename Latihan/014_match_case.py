hari = input("\nSekarang hari apa? : ").lower()

match hari:
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
        print("Sekarang lagi hari kerja!\n")
    case "sabtu" | "minggu":
        print("Sekarang lagi hari libur!\n")
    case _:
        print("Nama hari tidak valid!\n")