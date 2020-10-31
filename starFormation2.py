def starFormation2(n): #ini mendeklarasikan function
    kolom = n
    baris = n

    i = 0
    while(i < baris):
        j = n
        while(j > i):
            print("*", end="")
            j-=1
        print(" ")
        i+=1

#a = 4
#print(starFormation2(a))

