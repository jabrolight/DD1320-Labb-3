from bintreeFile import Bintree

def makeTree():
    tree = Bintree()
    data = input().strip()
    while data != "#":
        tree.put(data)
        data = input().strip()
    return tree

def searches(tree):
    findme = input().strip()
    while findme != "#":
        if findme in tree:
            print(findme, "found")
        else:
            print(findme, "not found")
        findme = input().strip()

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
 
def main():
    tree = makeTree()
    searches(tree)

main()