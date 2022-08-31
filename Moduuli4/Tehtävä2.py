# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan
# kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa.
tuumat = float(input("Syötä tuumat: "))
while tuumat > 0:
    sentit = tuumat * 2.54
    print(f"Syöttämäsi tuumat senttimetreinä: {sentit:.2f}")
    tuumat = float(input("Syötä tuumat: "))
