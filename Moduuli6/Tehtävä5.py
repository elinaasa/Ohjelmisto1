# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin
# parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
# Kirjoita testausta varten pääohjelma, jossa luot listan,
# kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.
lista = [1, 2, 3, 4, 5]

def parittomat(lista):
    for n in lista:
        if n % 2 == 0:
            lista.remove(n)
    return lista


print(lista)
print(parittomat(lista))
