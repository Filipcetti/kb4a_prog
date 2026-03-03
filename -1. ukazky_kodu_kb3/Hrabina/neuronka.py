import csv
from sklearn.neural_network import MLPClassifier

vstupy = []
vystupy = []

modely = {}
prevodovky = {}
paliva = {}

cesta = cesta = "C:/Users/filip/OneDrive - Střední škola informatiky, poštovnictví a finančnictví Brno/programování/kb4a_prog/kb4a_prog-5/-1. ukazky_kodu_kb3/Hrabina/merc.csv"

def preved(text, slovnik):
    if text not in slovnik:
        slovnik[text] = len(slovnik)
    return slovnik[text]

with open(cesta, encoding="utf-8") as soubor:
    ctecka = csv.DictReader(soubor)
    
    for radek in ctecka:
        model = preved(radek["model"], modely)
        prevodovka = preved(radek["transmission"], prevodovky)
        palivo = preved(radek["fuelType"], paliva)

        rok = int(radek["year"])
        najezd = float(radek["mileage"])
        dan = float(radek["tax"])
        spotreba = float(radek["mpg"])
        objem_motoru = float(radek["engineSize"])

        cena = int(float(radek["price"]) / 1000)  
        vstupy.append([model, prevodovka, palivo, rok, najezd, dan, spotreba, objem_motoru])
        vystupy.append(cena)

sit = MLPClassifier(hidden_layer_sizes=(10,), max_iter=500)

sit.fit(vstupy, vystupy)

predikce = sit.predict([vstupy[0]])

print("Predikovaná cena (v tisících):", predikce[0])
print("Predikovaná cena:", predikce[0] * 1000, "Kč")


"""
REPORT

Tento program slouží k jednoduché predikci ceny auta značky Mercedes
pomocí neuronové sítě.

Na vstupu je soubor merc.csv, kde jsou u každého auta uvedené
parametry jako model, rok výroby, nájezd, typ paliva,
převodovka, spotřeba, objem motoru atd.
Součástí je i cena auta, která je cílová hodnota.

Program nejdříve načte data pomocí knihovny csv.
Protože neuronová síť neumí pracovat s textem,
musím textové hodnoty (model, palivo, převodovka)
převést na čísla. To dělám pomocí slovníků,
kde každé nové hodnotě přiřadím číslo.

Číselné hodnoty (rok, nájezd, daň, spotřeba atd.)
převedu na int nebo float.

Cena se uloží jako výstup, ale ještě ji vydělím 1000,
aby nebyla moc velká (síť se tak učí lépe).

Všechny parametry auta se ukládají do seznamu vstupy
a ceny do seznamu vystupy.

Potom vytvořím neuronovou síť pomocí MLPClassifier
s jednou skrytou vrstvou o 10 neuronech.
Síť se učí pomocí metody fit() na všech datech
(nepoužívám rozdělení na trénovací a testovací).

Nakonec zkusím predikci na prvním autě ze seznamu
a vypíšu odhadovanou cenu.

Program tedy:
1) načte data
2) převede text na čísla
3) vytvoří neuronovou síť
4) naučí ji vztah mezi parametry auta a cenou
5) vypíše predikovanou cenu

Jedná se o jednoduchou školní ukázku použití
neuronové sítě v Pythonu.
"""