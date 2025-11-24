import random


def generuj_priklad():
    # generuje proiklad a vraci bool zda jej uživatel vyřešil
    cislo1 = random.randint(0, 9)
    operace = random.choice(["+", "-", "*"])
    cislo2 = random.randint(0, 9)

    print(f"Spočítej: {cislo1} {operace} {cislo2}")
    odpoved = int(input())

    if operace == "+":
        spravne = cislo1 + cislo2
    elif operace == "-":
        spravne = cislo1 - cislo2
    else:
        spravne = cislo1 * cislo2

    return odpoved == spravne


pocet_prikladu = random.randint(3, 6)
spravne_odpovedi = 0

for i in range(pocet_prikladu):
    if generuj_priklad():
        spravne_odpovedi += 1

print(f"Počet správných odpovědí: {spravne_odpovedi}")
