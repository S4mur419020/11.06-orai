import random

def lis_letrehozas():
    #generalj 100 véletlen szamot egész számot [-50, 150] között
    #a függyvény térjebn vissza a listával
    lista=[]
    i=0
    while i<100:
        vszam:int=int(random.random()*(151+50)-50)
        lista.append(vszam)
        i+=1
    return lista

lista=lis_letrehozas()
print(lista)


# a listában lévő számokat fűzd össze stringgé, az elválasztójel ; legyen az utolsó után ne legyen ;
def szovegge_alakit(lista):
    szoveg:str=""
    for i in range(0,len(lista),1):
        if i<len(lista):
            szoveg+=(f"{lista[i]};")
        else:
            szoveg+=(f"{lista[i]}")
    return szoveg
print(szovegge_alakit(lista))
szoveg_lista=szovegge_alakit(lista)
print(szoveg_lista)


def fajlba_mentes(szoveg):
    fajlom=open("adatok.txt","w",encoding='utf-8')
    fajlom.write(szoveg)
    fajlom.close()
    
fajlba_mentes(szoveg_lista)


def fajlbol_olvas(lista):
    fajlom=open("adatok.txt","w",encoding='utf-8')
    szoveg_fajbol:str=fajlom.read()
    szoveg_lista=szoveg_fajbol.split(";")
    lista=[]
    for i in range(0, len(szoveg_lista), 1):
        szam:int=int(szoveg_lista[i].strip())
        lista.append(szam)
    """(szoveg_fajbol)
    print(lista)"""
    fajlom.close()
    
    
def fel1(lista):
    i:int=0
    db:int=0
    while(i<len(lista)):
        print(lista[i])
        if(lista[i]<0):
            db+=1
        i+=1
        
    return db

def legnagyobb_szam(lista):
    max_index:int=0
    for i in range(0, len(lista, 1)):
        if(lista[i]>lista[max_index]):
            max_index+=i
            
    return lista[max_index]