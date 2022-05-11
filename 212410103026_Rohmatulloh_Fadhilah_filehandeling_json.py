import datetime
import os
import json
import datetime

file_data = 'Transaksi.json'
databases = []
rekap_pembelian= []
data_login = []



def clear():
    print ('\n')
    input ('Tekan enter untuk kembali ke menu utama!!!')
    #menu_utama()

def tambah_data():
    os.system('cls')
    show()
    nama = input ("Barang: ")
    jumlah = int (input("Jumlah: " ))
    harga = int (input("Harga: " ))
    item = ({"Barang": nama,
            "Jumlah": jumlah,
            "Harga": harga})
    databases.append(item)
    with open(file_data, 'w') as output:
            output.write(json.dumps(databases, indent=4))
    os.system('cls')


def parsing():
    with open(file_data, 'w') as output:
            output.write(json.dumps(databases, indent=1))


def kembali():
    with open(file_data,'r') as output:
        data = json.load(output)
        return data

def edit():
    with open (file_data,'w') as output:
        data = json.load(output)
        return data

def show():
    os.system('cls')
    datum = kembali()
    print ('List Daftar Obat '.center(40))
    print ('='*40)
    print ('|%-3s|%-10s   |%-5s  |%-8s  |'%('#',"Barang","Jumlah","Harga"))
    print ('='*40)
    for indek in range (len(datum)):
        indek +1
        print ('|%-3s|%-10s   |%-5s  | %-8s  |'%(indek, datum[indek]["Barang"],datum[indek]["Jumlah"], datum[indek]["Harga"]))
        
def menghapus():
    os.system('cls')
    show()
    datum = kembali()
    hapus = int(input('masukkan indek yang akan di hapus: '))
    datum.pop(hapus-1)
    parsing()
    os.system('cls')
    show()

def penjualan():
    os.system('cls')
    show()
    data = []
    datum = kembali()
    for i in datum:
        data.append(i)
    print ('Obat yang di Beli'.center(40))
    obat  = input('indeks obat yang di beli: ')
    jumlah = int(input('Banyak obat: '))
    bayar = int(input ('Nominal Pembayaran: '))
    for x in data :
        if x["Barang"] == obat:
            x ["Jumlah"] = ( int(x["Jumlah"]) - jumlah)
            total = int(x["Harga"]) * jumlah
            kembalian = bayar - total
            rekap_pembelian.append({"Barang" : x["Barang"],"Jumlah": jumlah,"Harga":x["Harga"],"total harga": total,"Uang": bayar, "Kembalian": kembalian})
            with open(file_data, 'w') as output:
                output.write(json.dumps(data, indent=4))
            


def rekap_pembayaran():
    os.system('cls')
    for i in  rekap_pembelian:
        print ('Slip Pembayaran'.center(40))
        print ('='*40)
        today = datetime.date.today()
        tanggal = today.strftime('%d-%m-%Y')
        print ('Tanggal           :\t',tanggal)
        print ('nama Barang       :\t',  i["Barang"])
        print ('Jumlah barang     :\t',i ["Jumlah"] )
        print ('Harga per pack    :\t', i["Harga"])
        print ('Nominal Pembayaran:\t', i ["Uang"])
        print ('Total Harga       :\t', i["total harga"])
        print ('Nominal Kembalian :\t', i["Kembalian"])
        print ('='*40)
        print('Terimakasih dan selamat Berbelanja Kembali')
        print ('='*40)
        break
def lis_menu ():
    daftar = ("""
            1. \t Tambah barang
            2. \t penjualan barang
            3. \t melihat data
            4. \t menghapus barang 
             """)
    print (daftar)


def menu_utama():
    while True:
        clear()
        lis_menu()
        menu = int(input('masukkan menu yang kalian pilih: '))
        if menu == 1:
            tambah_data()
        elif menu == 2:
            penjualan()
            rekap_pembayaran()
        elif menu == 3:
            show()
        elif menu == 4:
            menghapus()
        elif menu == 5:
            print (rekap_pembelian)
            break
        else:
            print ('Mohon maaf Menu Tersebut Tidak Tersedia!!!')



print ('-'*40)
print ('silahkan login terlebih dahulu'.center(30))
print ('='*40)
print (" 1. LOGIN \n 2. SIGUP")
simpan_login = []
while True:
    menu = int(input ('pilih menu yang kalian pilih [1] or [2]: '))
    if menu == 1:
        login = input ('masukkan username: ')
        passwd = input ('masukkan password: ')
        for i in range (len(simpan_login)):
            if login == simpan_login[i]["user"] and passwd == simpan_login [i]["password"]:
                print ("selamat Anda Berhasil Login")
                menu_utama()
            else:
                print("Username atau Password Yang anda Masukkan Salah!!!")
    elif menu == 2:
        log = input ('massukkan Username Baru: ')
        pas = input ('massukkan password: ')
        data = {"user": log, "password": pas}
        simpan_login.append(data)
        clear()
        continue

