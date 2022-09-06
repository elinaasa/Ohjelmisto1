# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa,
# onko se alkuluku. Alkulukuja ovat luvut,
# jotka ovat jaollisia vain ykkösellä ja itsellään.

luku = int(input("Syötä kokonaisluku: "))

for i in range(2, luku / 2 + 1):
    if luku % 2 == 0:
        print("Luku ei ole alkuluku.")
    else:
        print("Luku on alkuluku.")
