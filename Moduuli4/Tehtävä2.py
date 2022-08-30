# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan
# kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa.
tuumat = 1
sentit = float(input("Syötä senttimetrit: "))
while tuumat > 0:
    tuumat = sentit * 0.39370079
    print(f"Syöttämäsi senttimetrit tuumina: {tuumat:.2f}")
    sentit = float(input("Syötä senttimetrit: "))
