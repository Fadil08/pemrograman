import os
import datetime



databases = [{'Barang': 'paracetamol', 'Jumlah': 30, 'Harga': 5000},
            {'Barang': 'OBH Itrasal', 'Jumlah': 20, 'Harga': 7000},
            {'Barang': 'Hafilin', 'Jumlah': 20, 'Harga': 10000},
            {'Barang': 'promag', 'Jumlah': 20, 'Harga': 5000}]

daftar = ("""
            1. \t Tambah barang
            2. \t Kurangi barang
            3. \t melihat data
            4. \t menghapus barang 
            5. \t keluar
             """)

        
def insert ():
    os.system('cls')
    show()
    nama = input ('Barang: ')
    Jumlah = int(input ('Jumlah: '))
    harga = int(input ('Harga: '))
    databases.append({
        'Barang': nama,
        'Jumlah': Jumlah,
        'Harga': harga
    })
def show():
    os.system('cls')
    print ('List Barang'.center(40))
    print ('='*40)
    print ('|%-3s|%-10s   |%-5s  |%-8s  |'%('#','Barang', 'Jumlah', 'Harga'))
    print ('='*40)
    for indek in range (len(databases)):
        print ('|%-3s|%-10s   |%-5s  |%-8s  |'%(indek, databases[indek]['Barang'],databases[indek]['Jumlah'], databases[indek]['Harga']))
def menghapus():
    os.system('cls')
    show()
    hapus = int(input('masukkan indek yang akan di hapus: '))
    databases.pop(hapus)
    os.system('cls')
    show()
rekap_pembelian= []
def penjualan():
    os.system('cls')
    show()
    print ('Barang yang di Beli'.center(40))
    obat  = input('indeks obat yang di beli: ')
    jumlah = int(input('Banyak obat: '))
    bayar = int(input ('Nominal Pembayaran: '))
    for i in databases:
        if i['Barang'] == obat:
            i ['Jumlah'] = ( int(i['Jumlah']) - jumlah)
            total = int(i['Harga']) * jumlah
            kembalian = bayar - total
            rekap_pembelian.append({'barang' : i['Barang'],'jumlah': jumlah,'harga':i['Harga'],'total harga': total,'uang': bayar, 'kembalian': kembalian})
def rekap_pembayaran():
    os.system('cls')
    for i in  rekap_pembelian:
        print ('Slip Pembayaran'.center(40))
        print ('='*40)
        today = datetime.date.today()
        tanggal = today.strftime('%d-%m-%Y')
        print ('Tanggal           :\t',tanggal)
        print ('nama Barang       :\t',  i['barang'])
        print ('Jumlah barang     :\t',i ['jumlah'] )
        print ('Harga per pack    :\t', i['harga'])
        print ('Nominal Pembayaran:\t', i ['uang'])
        print ('Nominal Kembalian :\t', i['kembalian'])
        print ('='*40)
        print('Terimakasih dan selamat Berbelanja Kembali')
        print ('='*40)
        break
    
def clear():
    print ('\n')
    input ('Tekan enter untuk kembali ke menu utama!!!')
   
            

def utama ():
    while True:
        clear()
        print (''.join(daftar))
        menu = int(input('masukkan menu yang kalian pilih: '))
        if menu == 1:
            insert()#show data
        elif menu == 2:
            penjualan()
            rekap_pembayaran()#tambah data
        elif menu == 3:
            show()
            # apabila su bernilai 0 akan di hapus
        elif menu == 4:
            menghapus()
        elif menu == 5:
            print ('exit')
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
                utama()
            else:
                print("Username atau Password Yang anda Masukkan Salah!!!")
    elif menu == 2:
        log = input ('massukkan Username Baru: ')
        pas = input ('massukkan password: ')
        data = {"user": log, "password": pas}
        simpan_login.append(data)
        clear()
        continue

    
