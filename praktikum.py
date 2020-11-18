print("Nama : Febro Herdyanto")
print("NIM : 312010043")
print("Kelas : TI>20.B.1")
print("===========================")
print("Latihan - Modul Praktikum 4")
print()
print()

# Progammemintamemasukkandatasebanyak-banyaknya(gunakanperulangan)
# Tampilkanpertanyaanuntukmenambahdata(y/t?),apabilajawabant(Tidak),
# makaprogramakanmenampilkandaftardatanya.
# NilaiAkhirdiambildariperhitungan3komponennilai(tugas:30%,uts:35%,uas:35%)
akhir = []
stop = False

# Mengisi Nilai
while (not stop):
    nama = input("Masukkan Nama : ")
    nim = input("Masukkan NIM : ")
    tugas = input("Masukkan Nilai Tugas : ")
    uts = input("Masukkan Nilai UTS : ")
    uas = input("Masukkan Nilai UAS : ")
    nilai_akhir = 0.3 * float(tugas) + 0.35 * float(uts) + 0.35 * float(uas)
    akhir.extend([nama, nim, tugas, uts, uas, nilai_akhir])

    tanya = input("Tambah data? (y/n) : ")
    if (tanya == "n"):
        stop = True

# Cetak semua nilai

print("==============================")
print()

from prettytable import PrettyTable
x = PrettyTable()
x.field_names=["No","Nama","NIM","Tugas","UTS","UAS","Nilai Akhir"]
x.add_row([len(akhir[0]),akhir[0],akhir[1],akhir[2],akhir[3],akhir[4],akhir[5]])
print(x)
