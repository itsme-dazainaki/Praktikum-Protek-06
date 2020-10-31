def faktorial(n): #mendeklarasikan function
    i=1
    faktor = 1  
    while(i<=n):
        faktor = faktor* i #mengalikan faktor dan 1, lalu simpan lagi ke faktor
        i+=1 #increment
    return faktor

def combinasi(a,b): #mendeklarasikan function
    c=(faktorial(a) // (faktorial(b) * (faktorial(a-b) ) ) ) #rumus kombinasi
    return c

def permutasi(a,b): #mendeklarasikan function
    p=(faktorial(a) // faktorial(a-b)) #rumus permutasi
    return p

a = 5
b = 3
print(combinasi(a,b))

c = 10
d = 7
print(permutasi(c,d))

