# Kirjoita ohjelma, joka kysyy käyttäjän
# biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen,
# normaali vai korkea.
try:
    sukupuoli = input("Anna sukupuolesi: ")
    hemoglobiini = float(input("Anna hemoglobiiniarvosi: "))
except:
    print("Syöte on virheellinen.")

hemoglobiini = 0

# naiset
if sukupuoli.lower() == 'nainen':
    if hemoglobiini < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 117 <= hemoglobiini <= 175:
        print("Hemoglobiiniarvosi on normaali.")
    elif hemoglobiini > 175:
        print("Hemoglobiiniarvosi on korkea.")

# miehet
if sukupuoli.lower() == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 134 <= hemoglobiini <= 195:
        print("Hemoglobiiniarvosi on normaali.")
    elif hemoglobiini > 195:
        print("Hemoglobiiniarvosi on korkea.")
