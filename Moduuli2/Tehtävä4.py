# Kirjoita ohjelma, joka kysyy kolme kokonaislukua.
# Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.
luku1 = float(input("Syötä ensimmäinen kokonaisluku: "))
luku2 = float(input("Syötä toinen kokonaisluku: "))
luku3 = float(input("Syötä kolmas kokonaisluku: "))
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3
print("Lukujen summa on: " + str(summa))
print("Lukujen tulo on: " + str(tulo))
print("Lukujen keskiarvo on: " + str(keskiarvo))
