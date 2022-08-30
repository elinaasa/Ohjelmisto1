# rahat = float(input("Paljonko sinulla on rahaa? "))
# if rahat >=5:
#     print("Voit ostaa latten.")
# else:
#     print("Et voi ostaa lattea.")
# print("Kiitos testaamisesta.")

# pituus = float(input("Kuinka pitkä olet? "))
    # if 1.5 <= pituus <= 2.0:
   # print("Olet normaalipituinen.")
# if pituus >= 1.5 and pituus <= 2.0:
    # print("Olet normaalipituinen")
# if pituus <1.5 or pituus > 2.0:
    # print("Et ole normaalimittainen.")

# mjono1 = input("Anna eläinlaji: ")
# mjono2 = input("Anna eläinlaji: ")

# if mjono1 == mjono2:
#    print("Annoit saman eläinlajin.")

ika = int(input("Anna ikäsi: "))
if ika >= 15 and ika < 18:
    paino = float(input("Anna painosi: "))
if ika >= 18 or (ika >= 15 and paino >= 55):
    print("Lääkkeen käyttö sallittu.")
else:
    print("Lääkkeen käyttö ei sallittu.")
