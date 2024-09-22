nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))
tb = int(input("Masukkan tinggi badan: "))
#print(f"Halo {nama}, umur kamu {umur} tahun, dan tinggi badan {tb} cm")

if umur < 18:
    next = 18 - umur
if 35 > umur >= 18 and tb >= 160:
    print(f"Selamat saudara/i {nama} termasuk dalam kategori penerimaan Mahasiswa Baru")
elif umur < 18 and tb >= 160:
    print(f"Maaf saudara/i {nama} daftar lagi {next} tahun lagi ya")
else:
    print(f"Maaf saudara/i {nama} tidak termasuk dalam kategori penerimaan Mahasiswa Baru")
