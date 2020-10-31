def isPythagoras(a,b,c = 0) : #ini mendeklarasikan function
    hasil = (a*a)+(b*b)==(c*c)
    return hasil

a = 8
b = 6
c = 10

#menampilkan output dari pengecekan a,b,c dengan function isPythagoras
print("a =",a, ",","b =", b,",","c =", c, "-->", isPythagoras(a,b,c))