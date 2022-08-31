# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin:
# Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
import random
luku = random.randint(1, 10)
arvaus = 0
# print(luku)
while arvaus != luku:
    try:
        arvaus = float(input("Arvaa numero: "))
        if luku > arvaus:
            print("Liian pieni arvaus.")
        elif arvaus > luku:
            print("Liian suuri arvaus.")
    except ValueError:
        print("Virheellinen syöte.")
print("Oikein.")
