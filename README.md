# Pertemuan 9 - Praktikum 4 (*repo : p9_praktikum4*)
Tugas Pertemuan 9 - Praktikum 4 (Bahasa Pemrograman)
<hr>

= Nama  : Febro Herdyanto =<br>
= NIM   : 312010043       =<br>
= Kelas : TI.20.B.1       =<br>

Pada mata kuliah Bahasa Pemrograman - Pertemuan 9 kali ini saya mendapatkan materi *List, Tuple dan Dictionary*.<br>
Nah, untuk praktikum 4 ini materi yang didapatkan adalah **List**.<br>
<br>
* Didalam materi praktikum 4 ini terdapat 2 tugas. Yaitu : Latihan dan Praktikum.<br>

## Praktikum 4 - Praktikum

* Berikut adalah tugas dari Latihan, bisa dilihat pada gambar dibawah ini :<br>
![Soal Tugas Latihan](pict/soal_latihan.PNG)<br>
* Berikut jawaban / *source code* / program sederhana yang telah saya buat :
``` python
print("Nama : Febro Herdyanto")
print("NIM : 312010043")
print("Kelas : TI>20.B.1")
print("===========================")
print("Latihan - Modul Praktikum 4")
print()

print("Membuat List dengan 5 elemen")
daftar = [1, 2, 3, 4, 5]
print(daftar)
# Akses List
print("Menampilkan elemen ke 3")
print(daftar[2])

print("Ambil nilai elemen ke 2 sampai ke 4")
print(daftar[1:4])

print("Ambil nilai terakhir")
print(daftar[-1])

# Ubah element list
print("ubah elemen ke 4 dengan nilai lainnya")
daftar[3] = 8
print(daftar[3])

print("ubah elemen ke 4 sampai dengan elemen terakhir")
daftar[3:5] = [16, 20]
print(daftar)

# Tambah Element List
print("ambil 2 bagian dari list pertama(A) dan jadikan list ke2(B)")
baris = daftar[3:5]
print(baris)

print("tambah list B dengan nilai string")
baris.append("Febro")
print(baris)

print("Tambah list B dengan 3 nilai")
baris.append(["Herdyanto", 3, 2])
print(baris)

print("Menggabungkan list A dnegan List B")
gabung = daftar + baris
print(gabung)
```

* Untuk hasil dari source code tersebut adalah seperti berikut : <br>
![Hasil Soal Latihan](pict/hasil_latihan.PNG)<br>

Nah seperti itulah hasil dari program Latihan yang diberikan oleh dosen.<br>
<hr>

## Praktikum 4 - Praktikum