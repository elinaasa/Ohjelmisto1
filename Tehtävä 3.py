import math

# print("Hello")

# kayttaja = input('Anna nimesi: ')
# print("Hauska tavata, " + kayttaja + "!")

#Kirjoita ohjelma, joka kysyy ympyrän säteen
# ja tulostaa sen pinta-alan.

sade_str = input("Syötä ympyrän säde metreinä: ")
sade = float(sade_str)
pinta_ala = math.pi *sade ** 2
print(f"Ympyrän pinta-ala on: {pinta_ala:1.2f} neliömetriä.")

# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
# Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.


