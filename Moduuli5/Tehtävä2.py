# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.
import sys
lista = []
while True:
    luku = input("Syötä luku: ")
    if luku == "":
        break
    lista.append(int(luku))
    print(luku)
lista.sort(reverse=True)
print(str(lista))
