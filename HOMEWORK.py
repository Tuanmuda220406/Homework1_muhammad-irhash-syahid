# RENTAL MOBIL

print("============ RENTAL MOBIL ===========")
print("TEMPAT RENTAL MOBIL TERMURAH DI DUNIA")

print("\nDAFTAR MEREK MOBIL")
print("1. AVANZA - Rp 300.000/hari")
print("2. CIVIC - Rp 500.000/hari")
print("3. TOYOTA - Rp 400.000/hari")
print("4. KELUAR")

pilihan = input("Pilih opsi (1-4): ")

if pilihan == '1':
    print("Pilihan warna untuk AVANZA:")
    print("1. Merah")
    print("2. Putih")
    print("3. Hitam")
    warna = input("Pilih warna (1-3): ")
    jam = int(input("Berapa jam sewa? "))
    total_harga = 300000 * (jam / 24)
    print(f"Harga sewa AVANZA selama {jam} jam: Rp {total_harga:.2f}")
elif pilihan == '2':
    print("Pilihan warna untuk CIVIC:")
    print("1. Biru")
    print("2. Hitam")
    print("3. Putih")
    warna = input("Pilih warna (1-3): ")
    jam = int(input("Berapa jam sewa? "))
    total_harga = 500000 * (jam / 24)
    print(f"Harga sewa CIVIC selama {jam} jam: Rp {total_harga:.2f}")
elif pilihan == '3':
    print("Pilihan warna untuk TOYOTA:")
    print("1. Silver")
    print("2. Hitam")
    print("3. Merah")
    warna = input("Pilih warna (1-3): ")
    jam = int(input("Berapa jam sewa? "))
    total_harga = 400000 * (jam / 24)
    print(f"Harga sewa TOYOTA selama {jam} jam: Rp {total_harga:.2f}")
elif pilihan == '4':
    print("Terima kasih, sampai jumpa!")
else:
    print("Opsi tidak valid. Silakan coba lagi.")
