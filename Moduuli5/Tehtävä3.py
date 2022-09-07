# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa,
# onko se alkuluku. Alkulukuja ovat luvut,
# jotka ovat jaollisia vain ykkösellä ja itsellään.

luku = int(input("Syötä kokonaisluku: "))
if luku == 1:
    print("Luku ei ole alkuluku.")
else:
    for i in range(2, luku // 2 + 1):
        if luku % i == 0:
            print("Luku ei ole alkuluku.")
            break
    else:
        print("Luku on alkuluku.")
