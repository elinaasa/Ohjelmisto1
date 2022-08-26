# Kirjoita ohjelma, joka kysyy kolme kokonaislukua.
# Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.
luku1 = int(input("Syötä ensimmäinen kokonaisluku: "))
luku2 = int(input("Syötä toinen kokonaisluku: "))
luku3 = int(input("Syötä kolmas kokonaisluku: "))
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = int(summa / 3)
print("Lukujen summa on: " + str(summa))
print("Lukujen tulo on: " + str(tulo))
print("Lukujen keskiarvo on: " + str(keskiarvo))
