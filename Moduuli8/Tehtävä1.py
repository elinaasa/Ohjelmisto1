# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja
# sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
def connect_database():
    return mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='Salainensana123',
         autocommit=True
         )
connection = connect_database()

def hae_icao(icao):
    sql = f"""SELECT name, municipality FROM airport WHERE ident="{icao.upper()}";"""
    cursor = connection.cursor()
    cursor.execute(sql)
    return cursor.fetchall()


tulos = hae_icao(input("Kirjoita lentoaseman ICAO-koodi: "))

for t in tulos:
    print("Lentokenttä", t[0], " sijaitsee kunnassa ", t[1])