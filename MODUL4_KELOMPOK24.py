from method import *
pembuka = login_method("KOST KUTANG", "KOST MAWAR", "KOST MELATI", "KOST KAKI")
pembuka.awal()

#function 
def user ():
    print("LOGIN BERHASIL\n")
    nama = str(input('MASUKAN NAMA LENGKAP: '))
    kost = int(input("PILIH KOST: "))
    while(True):
        if (kost == 1):
            print("SELAMAT DATANG DI KOST KUTANG\nFASILITAS: KOLAM RENANG DALAM DAN KAMAR MANDI LUAR")
            harga = 1500000
            print("HARGA: 1,5 jt / bulan")
            bulan = int(input("DURASI SEWA(BULAN):"))
            ht = harga * bulan
            print("TOTAL YANG HARUS DIBAYAR: ",ht)
            print("///////////////////////")
            print("TERIMA KASIH",nama,"SUDAH MEMPERCAYAI IBU KOST")
            break;
        elif (kost == 2):
            print("SELAMAT DATANG DI KOST MAWAR\nFASILITAS: AC DAN KAMAR MANDI DALAM")
            harga = 1900000
            print("HARGA: 1,9 jt / bulan")
            bulan = int(input("DURASI SEWA(BULAN):"))
            ht = harga * bulan
            print("TOTAL YANG HARUS DIBAYAR: ",ht)
            print("///////////////////////")
            print("TERIMA KASIH",nama,"SUDAH MEMPERCAYAI IBU KOST")
            break;
        elif (kost == 3):
            print("SELAMAT DATANG DI KOST MELATI\nFASILITAS: KOLAM IKAN DALAM DAN KAMAR MANDI LUAR")
            harga = 1700000
            print("HARGA: 1,7 jt / bulan")
            bulan = int(input("DURASI SEWA(BULAN):"))
            ht = harga * bulan
            print("TOTAL YANG HARUS DIBAYAR: ",ht)
            print("///////////////////////")
            print("TERIMA KASIH",nama,"SUDAH MEMPERCAYAI IBU KOST")
            break;
        elif (kost == 4):
            print("SELAMAT DATANG DI KOST KAKI\nFASILITAS: AC DAN KAMAR MANDI LUAR")
            harga = 2000000
            print("HARGA: 2 jt / bulan")
            bulan = int(input("DURASI SEWA(BULAN):"))
            ht = harga * bulan
            print("TOTAL YANG HARUS DIBAYAR: ",ht)
            print("///////////////////////")
            print("TERIMA KASIH",nama,"SUDAH MEMPERCAYAI IBU KOST")
            break;
        else:
            print("ERROR")
            break;

#function dengan return
def masuk(x):
    percobaan = 1
    for i in range (percobaan):
        if x == "RENAN":
            print(f"SELAMAT DATANG {x}")
            user()
            break;
        else:
            print("ID BELUM TERDAFTAR")
            
        
masuk(input("MASUKAN NAMA: "))