def sum(*allData): #definisikan function, ini jenis dinamic parameter
    tmbh = 0 #inisialisasi
    for bil in allData: 
        tmbh += bil #untuk menambahkan seluruh input di allData
    print("Jumlah seluruh bilangan : ", tmbh) #untuk menampilkan hasil (karena tidak disimpan)

def average(*allData): #definisikan function, ini jenis dinamic parameter
    sum = 0 #inisialisasi
    count = 0
    for data in allData:
        sum += data #untuk menambahkan bilangan
        count += 1 #untuk bilangan pembagi, berdasar jumlah bilangan
    rata = sum / count #bagi jum bilangan dengan jum data
    print("Rata-ratanya : ", rata) #untuk menampilkan hasil (karena tidak disimpan)

def maks(*allData): #definisikan function, ini jenis dinamic parameter
    mak = -100 #inisialisasi
    for bil in allData:
        if bil>mak: #cek bil apakah lebih besar dari pembanding
            mak = bil 
    print("Nilai maksimalnya : ", mak) #untuk menampilkan hasil (karena tidak disimpan)

def min(*allData): #definisikan function, ini jenis dinamic parameter
    minim = 999 #inisialisasi
    for bil in allData:
        if (bil < minim):  #cek bil apakah lebih kecil dari pembanding
            minim = bil
    print("Nilai minimalnya : ", minim) #untuk menampilkan hasil (karena tidak disimpan)