# Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan
# leivisköinä, nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi
# ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.
leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))
massa = 13.3 * (luodit + (32 * (naulat + (20 * leiviskat))))
massakiloina = massa / 1000
massakiloina_int = int(massakiloina)
ylijaama = int((massakiloina - int(massakiloina)) * 1000)
print("Massa nykymittojen mukaan: " + str(massakiloina_int) + " kiloa ja " + str(ylijaama) + " grammaa.")
