# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 14:40:54 2021

@author: ASUS
"""

 #Siapkan variabel
print("===========================")
print(" APLIKASI 5c")
print(" Menampilkan Nilai Huruf")
print(" Bilangan Bulat 0-100")
print("===========================")
n=1
    
    #cek batasan inputan nilai 0-100
while n>=0 and n<=100:
        u = input(" Masukkan Nilai = ")
        n=int(u)
        if n>=0 and n<=100:
            if n>80:      
                sts=" Baik Sekali"
            elif n>=65:    
                sts=" Baik"
            elif n>=55:    
                sts=" Cukup"
            elif n>=40:    
                sts=" Kurang"
            else:               
                sts=" Kurang Sekali"
            print (sts)
            
            ulang = input(" Ulang program? y/t = ")
            if ulang=="t" or ulang=="T":
                break
        else:
            pesan=" Masukkan kembali angka nilai antara 0-100"
            print(pesan)