# Kirjoita while-toistorakennetta käyttävä ohjelma,
# joka tulostaa kolmella jaolliset
# luvut väliltä 1..1000.
i = 1
luku = 1
while i == luku:
    if 0 < luku < 1000 and luku % 3 == 0:
        print(i)
        i += 1
