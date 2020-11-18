print("Nama : Febro Herdyanto")
print("NIM : 312010043")
print("Kelas : TI>20.B.1")
print("===========================")
print("Latihan - Modul Praktikum 4")
print()
print()

daftar = []
stop = False

# Mengisi Nilai
while (not stop):
    nama = input("Masukkan Nama : ")
    nim = input("Masukkan NIM : ")
    tugas = input("Masukkan Nilai Tugas : ")
    uts = input("Masukkan Nilai UTS : ")
    uas = input("Masukkan Nilai UAS : ")
    nilai_akhir = 0.3 * float(tugas) + 0.35 * float(uts) + 0.35 * float(uas)
    daftar.extend([nama, nim, tugas, uts, uas, nilai_akhir])

    tanya = input("Tambah data? (y/n) : ")
    if (tanya == "n"):
        stop = True

# Cetak semua nilai

print("==============================")
print()


from prettytable import PrettyTable
x = PrettyTable()
x.field_names=["No","Nama","NIM","Tugas","UTS","UAS","Nilai Akhir"]
x.add_row([len(daftar[0]),daftar[0],daftar[1],daftar[2],daftar[3],daftar[4],daftar[5]])
print(x)
