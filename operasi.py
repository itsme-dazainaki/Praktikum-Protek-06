from operation import*

print("Hasil operasi 2 + 4 * 6 – 4 = ",kali(jumlah(2,4), kurang(6,4)))
print("Hasil operasi (4 + 7) * (6 - 9 = ", kali(jumlah(4,7), kurang(6,9)))
print("Hasil operasi (10 + 2) / (7 + 5) / (12 - 34)  = ", bagi(bagi(jumlah(10,2), jumlah(7,5)), kurang(12,34) ) )
