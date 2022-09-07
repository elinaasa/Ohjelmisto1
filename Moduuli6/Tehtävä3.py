# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
# ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän
# käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
def gallonat_litroina(gallonat):
    litrat = gallonat * 0.2641722
    return litrat


while True:
    gallonat = float(input("Syötä bensiinin määrä gallonina: "))
    if gallonat < 0:
        break
    tulos = gallonat_litroina(gallonat)
    print("Bensiinin määrä litroina: ", tulos)
