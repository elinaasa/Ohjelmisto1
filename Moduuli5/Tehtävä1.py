# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.
import random
nopat_maara = int(input("Syötä arpakuutioiden lukumäärä: "))
lista = []
for n in range(nopat_maara):
    noppa = random.randint(1, 6)
    lista.append(noppa)
summa = sum(lista)
# print(noppa)
# print(lista)
print(summa)
