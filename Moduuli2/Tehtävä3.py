# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
# Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.
kanta = float(input("Anna suorakulmion kanta metreinä: "))
korkeus = float(input("Anna suorakulmion korkeus metreinä: "))
piiri = kanta * 2 + korkeus * 2
ala = kanta * korkeus
print(f"Suorakulmion piiri on: {piiri:.2f} metriä.")
print(f"Suorakulmion pinta-ala on: {ala:.2f} metriä.")
