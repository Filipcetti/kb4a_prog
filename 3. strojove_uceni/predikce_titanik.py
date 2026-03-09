# Neuronová síť predikující BMI kategorii
# Jedná se pouze o učební ukázku - pro BMi je jinak využití neuronky nevhodné

import csv

# ZMĚNA: Nutno načíst nové knihovny
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

# ---------- Načtení CSV a úprava dat ----------
X = []  # = vstupy
Y = []  # = výstupy

with open(r"3. strojove_uceni\data\titanic.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        age = float(row["Age"])
        p_class = float(row["Pclass"])
        # Na vstupu mohou být jen číselné vstupy:
        if row["Sex"] == "male":
            gender = 0
        else:
            gender = 1

        survived = int(row["Survived"])

        X.append([age, p_class, gender])
        Y.append(survived)


# ---------- Rozdělení na trénování a testování ----------
# ZMĚNA: split pomocí funkce
#   funcke má tu výhodu, že dataset zároveň promíchá

trening_X, test_X, trening_Y, test_Y  = train_test_split(
        X, Y,
        test_size=0.2,
        random_state=42)

# ---------- Neuronová síť ----------
neural_network = MLPClassifier(
    hidden_layer_sizes=(16, 8), # změnou architektury lze zlepšit úspěšnost
    activation="relu",
    max_iter=2000,
    verbose=True,
    random_state=4
)

neural_network.fit(trening_X, trening_Y)

# ---------- Vyhodnocení ----------
results = neural_network.predict(test_X)

correct = 0
for i in range(len(results)):
    if test_Y[i] == results[i]:
        correct += 1
print("Přesnost:", correct / len(results))

# ---------- Confusion matrix ----------
# zobrazuje jaké odpovědi dává neuronka pro dané vstupy
ConfusionMatrixDisplay.from_predictions(
    test_Y, results)
plt.show()
