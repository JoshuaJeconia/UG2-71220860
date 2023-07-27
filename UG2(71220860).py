def volume_tabung(diameter, tinggi):
    jari_jari = diameter / 2
    volume = 3.14 * jari_jari**2  * tinggi
    return volume

def volume_kubus(sisi):
    volume = sisi ** 3
    return volume

def volume_balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume

print("==================== KALKULATOR CERDAS ====================")
print("Pilihlah bangun yang ingin anda hitung (inputan angka saja): ")
print("1. Tabung")
print("2. Kubus")
print("3. Balok")

pilihan = int(input(">> "))

if pilihan == 1:
    diameter = float(input("Masukkan diameter (cm) : "))
    tinggi = float(input("Masukkan tinggi (cm) : "))
    volume_tabung = volume_tabung(diameter, tinggi)
    print("Volume tabung adalah ", volume_tabung, "cm")
elif pilihan == 2:
    sisi = int(input("Masukkan sisi (cm) : "))
    volume_kubus = volume_kubus(sisi)
    print("Volume kubus adalah", volume_kubus, "cm")
elif pilihan == 3:
    panjang = int(input("Masukkan panjang (cm) : "))
    lebar = int(input("Masukkan lebar (cm) : "))
    tinggi = int(input("Masukkan tinggi (cm) : "))
    volume_balok = volume_balok(panjang, lebar, tinggi)
    print("Volume balok adalah", volume_balok, "cm")
else:
    print("Inputan yang anda masukkan salah !!")
