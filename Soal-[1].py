#!/usr/bin/env python
# coding: utf-8

# In[ ]:


kontak_saya = {
    
}
def input_kontak():
    while True:
        nama_kontak = str(input("Barang yang ingin ditambahkan ke list:\n"))
        daftar_saya.append(nama_kontak)
        pilihan = str(input("Ingin menambahkan lagi? Y/N"))
        if pilihan == 'Y' or pilihan == 'y' :
            pass
        elif pilihan == 'N' or pilihan == 'n' :
            return
        else :
            print("Pilihan tidak tersedia")
def print_barang():
    for i in range(len(kontak)):
        print(f"Barang ke: {i}, Nama Barang: {b}")
while True:
    print("+===Selamat Datang!===+")
    print("tekan 1 untuk menambah")
    print("tekan 2 untuk melihat")
    print("tekan 3 untuk keluar")
    keinginan = int(input("Pilihan anda :"))
    if keinginan == 1:
        input_kontak()
    if keinginan == 2:
        print_kontak()
    if keinginan == 3:
        print("Anda keluar!")
    else :
        print("Pilihan tidak tersedia")

