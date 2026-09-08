class Node: 
    def __init__(self, value, left= None, right= None):
        self.value= value
        self.right= right
        self.left= left


class Bintree:
    def __init__(self):
        self.root= None

    def put(self,newvalue):
        # Sorterar in newvalue i trädet
        
        self.root = putta(self.root,newvalue)

    def __contains__(self,value):
        # True om value finns i trädet, False annars
        return finns(self.root,value)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")


def putta(p, newvalue):
    if p== None:        
       return Node(newvalue)    #om trädet är tomt, skapa och gör p till rot
    if newvalue < p.value: 
        p.left= putta(p.left, newvalue) #kolla till vänster om p och lägg newvalue där om tomt
    if newvalue > p.value:
        p.right= putta(p.right, newvalue)   #kolla till vänster om p och lägg newvalue där om tomt
    return p     #returnera roten så att något allt pekar på trädet

def finns(p,value):
    if p == None:       # om trädet är tomt
        return False
    if value < p.value:     #kolla om det vänstra pekaren är mot värdet
        return finns(p.left, value)
    if value > p.value:     #kolla om det vänstra pekaren är mot värdet
        return finns(p.right, value)
    if value == p.value:    #kolla om pekaren redan är på värdet
        return True

    
def skriv(p):
    if p!= None:
        skriv(p.left)
        print(p.value)
        skriv(p.right)