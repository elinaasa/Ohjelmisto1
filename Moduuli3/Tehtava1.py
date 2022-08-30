
# Kirjoita ohjelma, joka kysyy kalastajalta kuhan
# pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea
# kuhan takaisin järveen
# ilmoittaen samalla käyttäjälle, montako senttiä
# alimmasta sallitusta
# pyyntimitasta puuttuu. Kuha on alamittainen,
# jos sen pituus on alle 37 cm.

kuha = float(input("Anna kuhan pituus senttimetreinä: "))
if kuha < 37:
    print("Kuha on alamittainen, laske se takaisin järveen. Pienin sallittu mitta on 37 cm.")
else:
    print("Hieno kala! :-)")
