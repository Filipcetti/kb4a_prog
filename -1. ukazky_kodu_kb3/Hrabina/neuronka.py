import csv
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

vstupy = []
vystupy = []

modely = {}
prevodovky = {}
paliva = {}

cesta = "C:\\Users\\st025470\\OneDrive - Střední škola informatiky, poštovnictví a finančnictví Brno\\programování\\kb4a_prog\\kb4a_prog-6\\-1. ukazky_kodu_kb3\\Hrabina\\merc.csv"

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

        cena = round(float(radek["price"]) / 10000)

        vstupy.append([model, prevodovka, palivo, rok, najezd, dan, spotreba, objem_motoru])
        vystupy.append(cena)


train_X, test_X, train_Y, test_Y = train_test_split(vstupy, vystupy, test_size=0.2)

sit = MLPClassifier(hidden_layer_sizes=(10,), max_iter=500)

sit.fit(train_X, train_Y)
 
predikce = sit.predict([vstupy[0]])

print("Predikovaná cena (v desítkách tisíc):", predikce[0])
print("Predikovaná cena:", predikce[0] * 10000, "Kč")

results = sit.predict(test_X)

correct = 0
for i in range(len(results)):
    if test_Y[i] == results[i]:
        correct += 1
print("Přesnost:", correct / len(results))


# Program jednoduché neuronové sítě na odhad ceny auta mercedes podle jeho parametrů. 
# Vstup sobor merc.csv kód se snaží najít souvislotsi mezi vlastnostmi auta. funkce preved kontroluje jsou vstupy
# uz ve slovniku nebo ne, kdy ne tak je prevede na cisla aby neuronka mohla fungovat.
# cenu si jeste vydelime 1000 aby nebyly velke hodnoty. parametry se ulozi do hodnoty vstupy a cena do vystupy.
#MLPClassifier a prikaz sit.fit(vstupy, vystupy) nauci sit vztahy mezi parametry.
#Program vypise odhadovanou cenu k prvnimu autu protoze predikce = sit.predict([vstupy[0]]). Kdyby byla v zavorce 2, udela to u tretiho auta atd.
