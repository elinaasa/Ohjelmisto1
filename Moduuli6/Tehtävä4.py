# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma,
# jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.
lista = [1, 2, 3, 4, 5]

def luvut(lista):
    summa = sum(lista)
    return summa


print(luvut(lista))
