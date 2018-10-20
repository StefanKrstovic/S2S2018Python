# print("Dobrodosli na S2S")
#
# def funkcija():
#    print("Ovo je funkcija")
#
#
# funkcija()
#
#
#
#
#

def prvi_veci(broj1, broj2):
    return broj1 > broj2


def vrati_najveci(b1, b2, b3):
    return max(b1, b2, b3)


def stampaj_najveci(b1, b2, b3, b4=0):
    print(max(b1, b2, b3))


broj1 = 5
broj2 = 4
broj3 = 6

# print(prvi_veci(broj3, broj2))

studenti = ["Mirko", "Zarko", "Darko"]

# for student in studenti:
#     print(student)

najveci = vrati_najveci(broj1, broj2, broj3)


# print(najveci)

# stampaj_najveci(broj1,broj2,broj3)
# stampaj_najveci(b2=2,b1=3)

def bolji_sum(*args):
    suma = 0
    print(*args)
    for a in args:
        suma = suma + a

    return suma


def funkcija(*args, broj1, broj2):
    pass


def stampaj(*args):
    for broj in args:
        if broj == 5:
            continue
        print(broj)

        if broj == 9:
            return

        # if broj==8:
        #     break

    print("Kraj")


# stampaj(1,2,3,4,5,6,7,8,9,10)

# print("Vracen je broj", broj)


# funkcija(1,3,4,6,broj1=2, broj2=5)

# brzawhile=0
# while brzawhile<10:
#     print(brzawhile)
#     brzawhile+=1


def stampaj_br_cifara(broj):
    broj = int(broj)
    slova = str(broj)
    print(len(slova))


# stampaj_br_cifara(123456789111111111)

# korak_po_korak
# optimizacija

import math


def da_li_je_prost(broj):
    if broj == 1 or broj == 0:
        return False

    if broj == 2:
        print(broj)
        return True

    if broj % 2 == 0:
        return False

    krajnji = int(math.sqrt(broj)) + 1
    for i in range(3, krajnji, 2):
        if broj % i == 0:
            return False

    print(broj)
    return True


def prvih_100_prostih():
    broj = 0
    counter = 0

    while (counter < 101):
        if da_li_je_prost(broj):
            counter += 1
        broj += 1


# prvih_100_prostih()

def sumiraj_rek(niz):
    if len(niz) == 0:
        return 0

    return niz[0] + sumiraj_rek(niz[1:])


# print(sumiraj_rek([1,2,3]))

from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonaci(redniBr):
    if redniBr == 1 or redniBr == 2:
        return 1

    return fibonaci(redniBr - 1) + fibonaci(redniBr - 2)


for i in range(1, 1001):
    print(i, ": ", fibonaci(i))