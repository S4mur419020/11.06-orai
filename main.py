import fajlkezeles

lista=fajlkezeles.fajlbol_olvas()



print("Első feladat.")
db:int=fajlkezeles.fel1(lista)
print(f"A negatív számok száma: {db}")

max_index:int=fajlkezeles.legnagyobb_szam(lista)
print(f"A legnagyobb szám az a {max_index}")