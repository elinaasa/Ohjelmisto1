# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan
# senttimetreinä sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan
# yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan
# halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle
# (eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
import math


def pizza(halkaisija, hinta):
    pinta_ala = math.pi * (halkaisija / 2) ** 2
    value = pinta_ala / hinta
    return value


hinta1 = float(input("Syötä 1. pizzan hinta: "))
halkaisija1 = float(input("Syötä 1. pizzan halkaisija: "))
hinta2 = float(input("Syötä 2. pizzan hinta: "))
halkaisija2 = float(input("Syötä 2. pizzan halkaisija: "))
value1 = pizza(halkaisija1, hinta1)
value2 = pizza(halkaisija2, hinta2)
if value1 < value2:
    print("2. pizza on parempi vaihtoehto.")
else:
    print("1. pizza on parempi vaihtoehto.")
