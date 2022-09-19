# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja
# tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
# että pieniä lentokenttiä on 65 kappaletta,
# helikopterikenttiä on 15 kappaletta jne.

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='Salainensana123',
    autocommit=True
)


def hae_lentokentta(iso_country):
    sql = f"""SELECT type FROM airport WHERE iso_country="{iso_country.upper()}";"""
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


maakoodi = input("Kirjoita maakoodi: ")
tulos = hae_lentokentta(maakoodi)
lentokentta_maarat = {}
for t in tulos:
    if t in lentokentta_maarat:
        lentokentta_maarat[t] += 1
    else:
        lentokentta_maarat[t] = 1

for key, value in lentokentta_maarat.items():
    print("Lentokenttätyyppiä", key[0], "on", value, "kappaletta.")
