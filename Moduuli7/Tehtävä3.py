# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
# hakea jo syötetyn lentoaseman tiedot vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen,
# ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin
# ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
# kunnes hän haluaa lopettaa.

lentokentat = {}


def lisaa_kentta():
    icao = input(print("Syötä lentoaseman ICAO-koodi: "))
    nimi = input(print("Syötä lentoaseman nimi : "))
    lentokentat[icao] = nimi
    return


def etsi_kentta():
    icao_input = input(print("Syötä kentän ICAO-koodi: "))
    if icao_input in lentokentat:
        nimi = lentokentat[icao_input]
    else:
        print("Lentokenttää ei löytynyt.")
    return


while True:
    user_input = input(print("Kirjoita 'uusi' jos haluat syöttää uuden lentoaseman, 'hae' jos haluat hakea jo "
                             "syötetyn lentoaseman, tai 'lopeta', jos haluat lopettaa."))
    if user_input.lower() == "uusi":
        lisaa_kentta()
    elif user_input.lower() == "hae":
        etsi_kentta()
    elif user_input.lower() == "lopeta":
        break
