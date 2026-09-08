from bintreeFile import Bintree
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ") 
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")

engelska =Bintree()
with open("engelska.txt", "r", encoding= "utf-8") as engelskafil:
    engelska_lista= engelskafil.read().split()
    for ord in engelska_lista:
        if ord not in engelska:
            engelska.put(ord)
            if ord in svenska:
                print(ord, end=" ")
