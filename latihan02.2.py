from starFormation1 import* #ini untuk mengimport function tadi, pemanggilnya sudah dihilangkan ya
from starFormation2 import* #ini untuk mengimport function tadi, pemanggilnya sudah dihilangkan ya

def starFormation3(n):   #ini function baru buat nyatuin 2 function sebelumnya
    starFormation1((n//2+1))
    starFormation2((n//2))

a=7 #ini nilai dari parameter n
starFormation3(a) #ini memanggil function 3
