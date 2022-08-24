import math

#Kirjoita ohjelma, joka kysyy ympyrän säteen
# ja tulostaa sen pinta-alan.

sade_str = input("Syötä ympyrän säde metreinä: ")
sade = float(sade_str)
pinta_ala = math.pi * (sade ** 2)
print(f"Ympyrän pinta-ala on: {pinta_ala:1.2f} neliömetriä.")
