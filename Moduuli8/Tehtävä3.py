# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
# Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
# Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
# Kirjoita hakukenttään geopy ja vie asennus loppuun.

import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="Salainensana123",
    autocommit=True
)


def sijainti(icao):
    sql = """SELECT latitude_deg, longitude_deg FROM airport WHERE ident = " + icaa + """
    cursor = connection.cursor()
    cursor.execute(sql)
    return cursor.fetchone()


sijainti1 = sijainti(input("Kirjoita lentoaseman ICAO-koodi: "))
sijainti2 = sijainti(input("Kirjoita lentoaseman ICAO-koodi: "))

etaisyys = distance.distance(sijainti1, sijainti2).miles * 1.609344

print(f"Lentoasemien välillä on {etaisyys:.2f}  km.")
