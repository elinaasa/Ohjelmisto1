# Kirjoita ohjelma, joka kysyy käyttäjältä laivan
# hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen
# kuvauksen alla olevan luettelon mukaisesti.
# Tehtävässä on käytettävä if/elif/else-toistorakennetta.
hyttiluokka = (input("Anna hyttiluokka: "))
if hyttiluokka.upper() == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka.upper() == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka.upper() == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka.upper() == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")
