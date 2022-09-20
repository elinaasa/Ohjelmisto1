# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja
# sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
import mysql.connector
def connect_database():
        return mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Salainensana123',
         autocommit=True
         )
connection = connect_database()


sql = "SELECT * FROM country WHERE iso_country='FI';"
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall() # type of result; list
for row in result:
    # type of row: tuple
    print(f"{row[0]}: {row[1]}, wikipedia: {row[3]}")
