def starFormation1(n): #ini mendeklarasikan function
    kolom = n
    baris = n

    i = 0
    while(i < baris):
        j = 0
        while(j <= i ):
            print("*", end="")
            j+=1
        print(" ")
        i+=1 

    
#a = 4 
#print(starFormation1(a)) #ini untuk menampilkan output sesuai input dengan function


