# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 12:16:46 2021

@author: AnggunYw_2E
"""

print ("=============================================")
print(" TRANSKASI BIAYA EKSPEDISI ")
print ("=============================================")
print(" Kode = A. Surabaya")
print(" Kode = B. Bandung")
print ("=============================================")

#jika menggunakan list Kode dibawah ini, maka metode yang digunakan
#adalah mendeteksi indeks value yang terpilih pada list kode.
#caranya: melakukan pencarian pada list kode menggunakan 
# nilai kode yang diinputkan
#salah satu metode : gunakan while
kode =['a','b']
#algoritma:
# baca berulang2 index dalam list kode, jika value sama dengan 
# value pilihan, ambil index nya

kota = ['surabaya','bandung']
jarak = [169,452]
ongkirperkm = [2500,4000]

pilihan = input(">> Masukkan Kode Tujuan = ")
#identifikasi pilihan
if pilihan=="a":
    idx = 0
elif pilihan=="b":
    idx = 1
else:
    idx = 0

#cetak tampilan layar
print(">>> Pilihan Tujuan = " + kota[idx])
print(">>> Jarak          = " + str(jarak[idx]) + " km")
print(">>> Ongkir per km  = Rp. " + str(ongkirperkm[idx]))

#hitung transksi
fixjarak = jarak[idx]
fixongkirkm = ongkirperkm[idx]
totongkir = fixjarak * fixongkirkm

#tampilkan total ongkir
print(">>>-------------------------------------")
print(">>> Total Biaya     = Rp." + str(totongkir))